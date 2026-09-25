"""Limpieza de datos Airbnb para la Fase 3.

preparar_filas selecciona las variables y descarta filas sin precio.
LimpiadorAirbnb aprende medianas en entrenamiento y las aplica a cualquier conjunto.
"""

import pandas as pd


def preparar_filas(df):
    """Selecciona las variables de Fase 2 y descarta filas sin precio."""
    objetivo = "price_quote_price_per_night"
    columnas = [
        "hosts_time_as_host_years", "neighbourhood_cleansed", "property_type",
        "room_type", "accommodates", "bathrooms", "bedrooms", "beds",
        objetivo, "number_of_reviews", "review_scores_rating",
        "review_scores_accuracy", "review_scores_cleanliness", "review_scores_checkin",
        "review_scores_communication", "review_scores_location", "review_scores_value",
    ]
    columnas_imputar = [
        "bathrooms", "bedrooms", "beds", "review_scores_rating",
        "review_scores_accuracy", "review_scores_cleanliness", "review_scores_checkin",
        "review_scores_communication", "review_scores_location", "review_scores_value",
    ]
    faltantes = [c for c in columnas if c not in df.columns]
    if faltantes:
        raise KeyError(f"Faltan columnas requeridas: {faltantes}")
    seleccion = df.loc[:, columnas].copy()
    for columna in [objetivo, *columnas_imputar]:
        if not pd.api.types.is_numeric_dtype(seleccion[columna]):
            raise TypeError(f"'{columna}' debe ser numérica; revisar la carga del archivo")
    antes = len(seleccion)
    seleccion = seleccion.dropna(subset=[objetivo]).copy()
    if seleccion.empty:
        raise ValueError("No quedan filas con precio conocido")
    informe = {
        "filas_recibidas": antes,
        "sin_precio_eliminadas": antes - len(seleccion),
        "filas_utilizables": len(seleccion),
    }
    return seleccion, informe


class LimpiadorAirbnb:
    """Imputa columnas numéricas usando medianas aprendidas solo en entrenamiento."""

    def __init__(self, columnas=None):
        if columnas is None:
            columnas = [
                "bathrooms", "bedrooms", "beds", "review_scores_rating",
                "review_scores_accuracy", "review_scores_cleanliness",
                "review_scores_checkin", "review_scores_communication",
                "review_scores_location", "review_scores_value",
            ]
        self.columnas = tuple(columnas)
        self._medianas = None

    @property
    def medianas(self):
        if self._medianas is None:
            raise RuntimeError("Primero se debe llamar a ajustar(entrenamiento)")
        return self._medianas.copy()

    def _verificar_columnas(self, df):
        faltantes = [c for c in self.columnas if c not in df.columns]
        if faltantes:
            raise KeyError(f"Faltan columnas para imputar: {faltantes}")
        no_numericas = [
            c for c in self.columnas if not pd.api.types.is_numeric_dtype(df[c])
        ]
        if no_numericas:
            raise TypeError(f"Columnas no numéricas: {no_numericas}")

    def ajustar(self, entrenamiento):
        """Aprende una mediana por columna usando solo entrenamiento."""
        self._verificar_columnas(entrenamiento)
        medianas = entrenamiento.loc[:, self.columnas].median()
        vacias = medianas[medianas.isna()].index.tolist()
        if vacias:
            raise ValueError(f"Sin valores observados en entrenamiento: {vacias}")
        self._medianas = medianas
        return self

    def transformar(self, df):
        """Rellena nulos usando las medianas previamente aprendidas."""
        valores = self.medianas
        self._verificar_columnas(df)
        resultado = df.copy()
        for columna in self.columnas:
            resultado[columna] = resultado[columna].fillna(valores[columna])
        return resultado

    def ajustar_transformar(self, entrenamiento):
        """Ajusta las medianas y transforma el mismo conjunto."""
        return self.ajustar(entrenamiento).transformar(entrenamiento)
