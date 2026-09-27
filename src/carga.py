"""Carga de datos para el proyecto Airbnb - Fase 3.

Este módulo centraliza la lectura de archivos CSV y Excel y valida
que la ruta de entrada exista antes de continuar con el pipeline.
"""

from pathlib import Path
import pandas as pd


def cargar_datos(ruta) -> pd.DataFrame:
    """Carga un dataset CSV o Excel desde una ruta local."""
    ruta = Path(ruta)

    if not ruta.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {ruta}")

    extension = ruta.suffix.lower()

    if extension == ".csv":
        df = pd.read_csv(ruta)
    elif extension in {".xls", ".xlsx"}:
        df = pd.read_excel(ruta)
    else:
        raise ValueError(
            f"Formato no compatible: {extension}. "
            "Utiliza un archivo CSV, XLS o XLSX."
        )

    print(
        f"Datos cargados correctamente: "
        f"{df.shape[0]:,} filas y {df.shape[1]} columnas"
    )
    return df.copy()
