"""
Módulo de Preprocesamiento y Transformación de Datos
===================================================
Este módulo contiene las funciones necesarias para aplicar One-Hot Encoding 
a variables categóricas y escalamiento de características continuas mediante RobustScaler.
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, RobustScaler


def codificar_one_hot(df: pd.DataFrame, columna: str) -> pd.DataFrame:
    """
    Codifica una columna categórica en variables binarias (One-Hot)
    manteniendo la alineación de índices del DataFrame original.
    """
    df_temp = df.copy()

    # 1. Label Encoding
    le = LabelEncoder()
    etiquetas = le.fit_transform(df_temp[columna])

    categorias = list(le.classes_)
    categorias.sort()

    # 2. One-Hot Encoding
    ohe = OneHotEncoder(sparse_output=False)
    matriz_ohe = ohe.fit_transform(etiquetas.reshape(-1, 1))

    # 3. Creación del DataFrame transformado
    nombres_columnas = [f"{columna}_{cat}" for cat in categorias]
    nuevas_cols = pd.DataFrame(
        matriz_ohe, columns=nombres_columnas, index=df_temp.index
    )

    # 4. Concatenación y eliminación de la columna original
    df_temp = df_temp.drop(columns=[columna])
    return pd.concat([df_temp, nuevas_cols], axis=1)


def escalar_caracteristicas(
    df: pd.DataFrame, columna_target: str = "price"
) -> pd.DataFrame:
    """
    Escala las variables numéricas continuas usando RobustScaler.
    Excluye la columna objetivo (target) y las columnas binarias (0 y 1).
    """
    df_escalado = df.copy()

    columnas_num = df_escalado.select_dtypes(
        include=["int64", "float64"]
    ).columns.tolist()

    # Filtrar columnas continuas que no sean el target ni binarias
    columnas_continuas = [
        col
        for col in columnas_num
        if col != columna_target
        and not set(df_escalado[col].unique()).issubset({0, 1})
    ]

    scaler = RobustScaler()
    df_escalado[columnas_continuas] = scaler.fit_transform(
        df_escalado[columnas_continuas]
    )

    return df_escalado


def ejecutar_pipeline_transformacion(
    df: pd.DataFrame, columnas_categoricas: list, columna_target: str = "price"
) -> pd.DataFrame:
    """
    Función principal que orquesta el proceso completo de transformación:
    1. Aplicación de One-Hot Encoding a la lista de columnas indicadas.
    2. Escalamiento de características continuas.
    """
    df_procesado = df.copy()

    for col in columnas_categoricas:
        if col in df_procesado.columns:
            df_procesado = codificar_one_hot(df_procesado, col)

    df_procesado = escalar_caracteristicas(
        df_procesado, columna_target=columna_target
    )

    return df_procesado
