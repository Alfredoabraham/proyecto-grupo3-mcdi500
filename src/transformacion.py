import os
import re
import numpy as np
import pandas as pd
from sklearn.preprocessing import RobustScaler


class PreprocesadorAirbnb:
    """Clase para la transformación y preparación de datos de Airbnb.

    Encapsula el pipeline de codificación One-Hot y escalamiento RobustScaler.
    """

    def __init__(self, ruta_archivo: str = None, df: pd.DataFrame = None):
        self.ruta_archivo = ruta_archivo
        self.df = df.copy() if df is not None else None
        self.df_analisis = None

    def cargar_datos(self) -> pd.DataFrame:
        """Carga el dataset desde la ruta configurada."""
        if not self.ruta_archivo or not os.path.exists(self.ruta_archivo):
            raise FileNotFoundError(
                f"Ruta de archivo no válida o no encontrada: {self.ruta_archivo}"
            )

        if self.ruta_archivo.endswith(".csv"):
            self.df = pd.read_csv(self.ruta_archivo)
        else:
            self.df = pd.read_excel(self.ruta_archivo)

        print(
            f"✓ Archivo cargado exitosamente. Dimensiones: {self.df.shape}"
        )
        return self.df

    def traducir_y_limpiar_categorias(self):
        """Traduce variables categóricas al español antes de codificar."""
        if self.df is None:
            raise ValueError("No hay datos cargados en el preprocesador.")

        # Traducción de tipo de habitación
        mapa_habitacion = {
            "Entire home/apt": "Casa/Apto entero",
            "Private room": "Habitación privada",
            "Shared room": "Habitación compartida",
            "Hotel room": "Habitación de hotel",
        }
        if "tipo_habitacion" in self.df.columns:
            self.df["tipo_habitacion"] = self.df["tipo_habitacion"].replace(
                mapa_habitacion
            )

        # Traducción de tipo de propiedad
        mapa_propiedad = {
            "Entire rental unit": "Unidad de arriendo entera",
            "Private room in rental unit": "Habitación privada en arriendo",
            "Shared room in rental unit": "Habitación compartida en arriendo",
            "Private room in home": "Habitación privada en casa",
            "Entire home": "Casa entera",
            "Private room in condo": "Habitación privada en condominio",
            "Shared room in hotel": "Habitación compartida en hotel",
        }
        if "property_type" in self.df.columns:
            self.df["property_type"] = self.df["property_type"].replace(
                mapa_propiedad
            )

    def filtrar_outliers_precio(
        self,
        columna_precio: str = "precio_por_noche",
        umbral_max: float = 2000000.0,
    ):
        """Filtra atípicos extremos de precio (ej.

        valores aberrantes de $97M).
        """
        if self.df is None:
            raise ValueError("No hay datos cargados.")

        if columna_precio in self.df.columns:
            filas_antes = len(self.df)
            self.df = self.df[
                (self.df[columna_precio] > 0)
                & (self.df[columna_precio] <= umbral_max)
            ].copy()
            filas_despues = len(self.df)
            print(
                f"✓ Outliers filtrados en '{columna_precio}'. Registros eliminados: {filas_antes - filas_despues}"
            )

    def guardar_base_analisis(self):
        """Guarda una copia antes de codificar para mantener variables legibles en el informe."""
        if self.df is None:
            raise ValueError("No hay datos cargados.")
        self.df_analisis = self.df.copy()

    @staticmethod
    def _limpiar_nombre_columna(nombre: str) -> str:
        """Formatea los nombres de las nuevas columnas binarias."""
        nombre_limpio = re.sub(r"[^\w\s]", "", str(nombre))
        return re.sub(r"\s+", "_", nombre_limpio).strip().lower()

    def codificar_one_hot(self, columna: str) -> pd.DataFrame:
        """Codifica una columna categórica en variables binarias (One-Hot)

        manteniendo la alineación de índices del DataFrame original.
        """
        if self.df is None:
            raise ValueError("No hay datos cargados.")

        if columna in self.df.columns:
            dummies = pd.get_dummies(self.df[columna], prefix=columna, dtype=int)
            dummies.columns = [
                self._limpiar_nombre_columna(col) for col in dummies.columns
            ]
            self.df = pd.concat(
                [self.df.drop(columns=[columna]), dummies], axis=1
            )
        return self.df

    def escalar_caracteristicas(
        self, columna_target: str = "precio_por_noche"
    ) -> pd.DataFrame:
        """Escala las variables numéricas continuas usando RobustScaler.

        Excluye la columna objetivo (target) y las columnas binarias (0 y 1).
        """
        if self.df is None:
            raise ValueError("No hay datos cargados.")

        columnas_num = self.df.select_dtypes(
            include=["int64", "float64", "int32"]
        ).columns.tolist()

        # Filtrar columnas continuas que no sean el target ni binarias
        columnas_continuas = [
            col
            for col in columnas_num
            if col != columna_target
            and not set(self.df[col].dropna().unique()).issubset({0, 1})
        ]

        scaler = RobustScaler()
        if columnas_continuas:
            self.df[columnas_continuas] = scaler.fit_transform(
                self.df[columnas_continuas]
            )

        return self.df

    def ejecutar_pipeline(
        self, columnas_categoricas: list, columna_target: str = "precio_por_noche"
    ) -> pd.DataFrame:
        """Orquesta el proceso completo de preprocesamiento y transformación."""
        if self.df is None:
            self.cargar_datos()

        self.traducir_y_limpiar_categorias()
        self.filtrar_outliers_precio(columna_precio=columna_target)
        self.guardar_base_analisis()

        for col in columnas_categoricas:
            self.codificar_one_hot(col)

        self.escalar_caracteristicas(columna_target=columna_target)
        return self.df

class PreprocesadorSantiago(PreprocesadorAirbnb):
    """Subclase especializada que hereda de PreprocesadorAirbnb."""

    def crear_variable_sector_oriente(self) -> pd.DataFrame:
        """Método especializado: Añade indicador binario para comunas del Sector Oriente."""
        if self.df is None:
            raise ValueError("No hay datos cargados.")

        comunas_oriente = [
            "Las Condes",
            "Providencia",
            "Vitacura",
            "Lo Barnechea",
            "La Reina",
            "Ñuñoa",
        ]
        if "comuna" in self.df.columns:
            self.df["es_sector_oriente"] = (
                self.df["comuna"].isin(comunas_oriente).astype(int)
            )
            print("✓ Creada la variable 'es_sector_oriente'.")
        return self.df
