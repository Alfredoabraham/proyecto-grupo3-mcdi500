class Validacion:
    """Objeto que guarda una tabla de datos y sabe prepararla para el analisis.

    La tabla vive en el atributo self.df. Cada metodo (cargar, limpiar, codificar,
    escalar, validar) es un paso del pipeline que trabaja sobre esa misma tabla.
    """

    def __init__(self, df):
        # __init__ es el constructor: deja listos los atributos del objeto.
        self.df = df        # donde esta el archivo de datos

    def validar(self):
        """Revisa que la tabla quedo sin nulos y sin texto sin codificar."""
        nulos = int(self.df.isnull().sum().sum())
        texto = self.df.select_dtypes(exclude=[np.number]).columns.tolist()
        print("Nulos totales:", nulos)
        print("Columnas de texto sin codificar:", texto if texto else "ninguna")
        print("Dimensiones finales:", self.df.shape)
        return nulos == 0 and not texto



