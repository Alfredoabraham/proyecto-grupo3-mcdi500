"""Carga de datos para el proyecto Airbnb - Fase 3.

Este módulo centraliza la lectura de archivos CSV, CSV.GZ y Excel y valida
que la ruta de entrada exista antes de continuar con el pipeline.
"""

from pathlib import Path
import pandas as pd


def cargar_datos(ruta) -> pd.DataFrame:
    """Carga un dataset CSV, CSV.GZ o Excel desde una ruta local."""
    ruta = Path(ruta)

    if not ruta.exists():
        raise FileNotFoundError(f"No se encontró el archivo: {ruta}")

    # Convertimos toda la ruta en minúsculas para revisar las extensiones compuestas
    nombre_archivo = ruta.name.lower()

    if nombre_archivo.endswith(".csv") or nombre_archivo.endswith(".csv.gz") or nombre_archivo.endswith(".gz"):
        df = pd.read_csv(ruta)
    elif nombre_archivo.endswith(".xls") or nombre_archivo.endswith(".xlsx"):
        df = pd.read_excel(ruta)
    else:
        raise ValueError(
            f"Formato no compatible: {ruta.suffix}. "
            "Utiliza un archivo CSV, CSV.GZ, XLS o XLSX."
        )

    print(
        f"Datos cargados correctamente: "
        f"{df.shape[0]:,} filas y {df.shape[1]} columnas"
    )
    return df.copy()