from abc import ABC, abstractmethod
import re
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, RobustScaler, OneHotEncoder


class EstrategiaEscalamiento(ABC):
    """Interfaz abstracta para estrategias de estandarización/escalamiento."""
    @abstractmethod
    def fit(self, df: pd.DataFrame, columnas: list):
        pass

    @abstractmethod
    def transform(self, df: pd.DataFrame, columnas: list) -> pd.DataFrame:
        pass


class EstrategiaStandard(EstrategiaEscalamiento):
    """Estrategia de escalamiento con StandardScaler (Media y Desviación Estándar)."""
    def __init__(self):
        self._scaler = StandardScaler()

    def fit(self, df: pd.DataFrame, columnas: list):
        self._scaler.fit(df[columnas])

    def transform(self, df: pd.DataFrame, columnas: list) -> pd.DataFrame:
        df_res = df.copy()
        df_res[columnas] = self._scaler.transform(df[columnas])
        return df_res


class EstrategiaRobust(EstrategiaEscalamiento):
    """Estrategia de escalamiento con RobustScaler (Mediana y Rango Intercuartílico)."""
    def __init__(self):
        self._scaler = RobustScaler()

    def fit(self, df: pd.DataFrame, columnas: list):
        self._scaler.fit(df[columnas])

    def transform(self, df: pd.DataFrame, columnas: list) -> pd.DataFrame:
        df_res = df.copy()
        df_res[columnas] = self._scaler.transform(df[columnas])
        return df_res


class Transformador(ABC):
    """Clase base abstracta para todos los pasos de transformación."""
    def __init__(self):
        self._ajustado = False

    @abstractmethod
    def ajustar(self, df: pd.DataFrame):
        """Aprende parámetros sobre el conjunto de datos de entrada."""
        pass

    @abstractmethod
    def transformar(self, df: pd.DataFrame) -> pd.DataFrame:
        """Aplica la transformación aprendida sobre un DataFrame."""
        pass

    def _verificar_ajustado(self):
        if not self._ajustado:
            raise RuntimeError("El transformador debe ser ejecutado en ajustar() antes de transformar().")



class CodificadorNominal(Transformador):
    """Transformador de variables categóricas mediante One-Hot Encoding."""
    def __init__(self, columna: str, prefijo: str):
        super().__init__()
        self._columna = columna
        self._prefijo = prefijo
        self._encoder = None
        self._categorias = None
        self._nombres_nuevos = None

    @staticmethod
    def _limpiar_nombre(texto: str) -> str:
        texto = str(texto).strip().replace("/", "_")
        texto = re.sub(r"[^0-9A-Za-zÁÉÍÓÚáéíóúÑñ]+", "_", texto)
        return texto.strip("_")

    def ajustar(self, df: pd.DataFrame):
        if self._columna not in df.columns:
            raise KeyError(f"La columna '{self._columna}' no está presente en el DataFrame.")
        self._categorias = sorted(df[self._columna].astype(str).unique())
        self._encoder = OneHotEncoder(
            categories=[self._categorias],
            sparse_output=False,
            handle_unknown="ignore"
        )
        self._encoder.fit(df[[self._columna]].astype(str))
        self._nombres_nuevos = [f"{self._prefijo}_{self._limpiar_nombre(c)}" for c in self._categorias]
        self._ajustado = True
        return self

    def transformar(self, df: pd.DataFrame) -> pd.DataFrame:
        self._verificar_ajustado()
        if self._columna not in df.columns:
            raise KeyError(f"La columna '{self._columna}' no está presente en el DataFrame.")
        
        df_res = df.copy()
        matriz = self._encoder.transform(df_res[[self._columna]].astype(str))
        df_encoded = pd.DataFrame(matriz, columns=self._nombres_nuevos, index=df_res.index).astype(int)
        
        df_res = pd.concat([df_res.drop(columns=[self._columna]), df_encoded], axis=1)
        return df_res


class EscaladorFlexible(Transformador):
    """Transformador de estandarización que delega el cálculo a una Estrategia (Strategy Pattern)."""
    def __init__(self, columnas: list, estrategia: EstrategiaEscalamiento):
        super().__init__()
        self._columnas = columnas
        self._estrategia = estrategia

    def ajustar(self, df: pd.DataFrame):
        columnas_faltantes = [c for c in self._columnas if c not in df.columns]
        if columnas_faltantes:
            raise KeyError(f"Columnas faltantes para escalamiento: {columnas_faltantes}")
        self._estrategia.fit(df, self._columnas)
        self._ajustado = True
        return self

    def transformar(self, df: pd.DataFrame) -> pd.DataFrame:
        self._verificar_ajustado()
        return self._estrategia.transform(df, self._columnas)


class ImputadorMediana(Transformador):
    """Imputa valores nulos en variables numéricas utilizando la mediana aprendida."""
    def __init__(self, columnas: list = None):
        super().__init__()
        self._columnas = columnas
        self._medianas = {}

    @property
    def medianas(self) -> dict:
        self._verificar_ajustado()
        return self._medianas.copy()

    def ajustar(self, df: pd.DataFrame):
        target_cols = self._columnas if self._columnas else df.select_dtypes(include=np.number).columns
        for c in target_cols:
            self._medianas[c] = df[c].median()
        self._ajustado = True
        return self

    def transformar(self, df: pd.DataFrame) -> pd.DataFrame:
        self._verificar_ajustado()
        df_res = df.copy()
        for c, med in self._medianas.items():
            if c in df_res.columns:
                df_res[c] = df_res[c].fillna(med)
        return df_res



class Pipeline:
    """Orquestador secuencial que ejecuta pasos transformadores aplicando Polimorfismo."""
    def __init__(self, pasos: list):
        self._pasos = pasos

    def ejecutar(self, df: pd.DataFrame) -> pd.DataFrame:
        df_transformado = df.copy()
        for paso in self._pasos:
            # Bucle polimórfico: cada paso implementa ajustar() y transformar()
            df_transformado = paso.ajustar(df_transformado).transformar(df_transformado)
        return df_transformado