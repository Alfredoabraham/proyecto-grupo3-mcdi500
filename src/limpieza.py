def preparar_filas(df):
    faltantes = [c for c in COLUMNAS if c not in df.columns]
    if faltantes:
        raise KeyError(f"Faltan columnas requeridas: {faltantes}")
    seleccion = df.loc[:, COLUMNAS].copy()
    # Fallar de forma explícita si números llegaron como texto; no convertir silenciosamente.
    for columna in [OBJETIVO, *COLUMNAS_IMPUTAR]:
        if not pd.api.types.is_numeric_dtype(seleccion[columna]):
            raise TypeError(f"'{columna}' debe ser numérica; revisar la carga del archivo")
    antes = len(seleccion)
    seleccion = seleccion.dropna(subset=[OBJETIVO]).copy()
    if seleccion.empty:
        raise ValueError("No quedan filas con precio conocido")
    informe = {"filas_recibidas": antes, "sin_precio_eliminadas": antes - len(seleccion),
               "filas_utilizables": len(seleccion)}
    return seleccion, informe
    
class LimpiadorAirbnb:
    """Imputación por mediana para las variables numéricas de Fase 2."""

    def __init__(self, columnas=COLUMNAS_IMPUTAR):
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
        no_numericas = [c for c in self.columnas
                        if not pd.api.types.is_numeric_dtype(df[c])]
        if no_numericas:
            raise TypeError(f"Columnas no numéricas: {no_numericas}")

    def ajustar(self, entrenamiento):
        self._verificar_columnas(entrenamiento)
        medianas = entrenamiento.loc[:, self.columnas].median()
        vacias = medianas[medianas.isna()].index.tolist()
        if vacias:
            raise ValueError(f"Sin valores observados en entrenamiento: {vacias}")
        self._medianas = medianas
        return self

    def transformar(self, df):
        valores = self.medianas
        self._verificar_columnas(df)
        resultado = df.copy()
        for columna in self.columnas:
            resultado[columna] = resultado[columna].fillna(valores[columna])
        return resultado

    def ajustar_transformar(self, entrenamiento):
        return self.ajustar(entrenamiento).transformar(entrenamiento)