import numpy as np

import pandas as pd
import numpy as np
import re


class Validacion:
    """
    Clase encargada de validar el resultado final del pipeline.

    Permite:
    - comprobar que el DataFrame no tenga nulos;
    - comprobar que no queden columnas de texto sin codificar;
    - comparar el resultado de Fase 3 contra el conjunto
      procesado obtenido en Fase 2.
    """

    def __init__(self, df):
        """
        Recibe el DataFrame resultante del pipeline de Fase 3.
        """

        if not isinstance(df, pd.DataFrame):
            raise TypeError(
                "El objeto recibido debe ser un DataFrame de pandas."
            )

        self.df = df


    def validar(self):
        """
        Revisa que la tabla final no esté vacía,
        no tenga nulos ni columnas de texto sin codificar.
        """

        # Caso límite: DataFrame vacío
        assert not self.df.empty, (
        "El DataFrame está vacío."
    )        
         
        nulos = int(self.df.isnull().sum().sum())

        texto = (
            self.df
            .select_dtypes(exclude=[np.number])
            .columns
            .tolist()
        )

        print("Nulos totales:", nulos)
        print(
            "Columnas de texto sin codificar:",
            texto if texto else "ninguna"
        )
        print("Dimensiones finales:", self.df.shape)

        assert nulos == 0, (
            f"Se encontraron {nulos} valores nulos."
        )

        assert len(texto) == 0, (
            f"Quedan columnas de texto sin codificar: {texto}"
        )

        return True


    @staticmethod
    def _normalizar_nombre_columna(nombre):
        """
        Crea un nombre común para poder comparar las columnas
        de Fase 2 y Fase 3.

        Esta normalización se utiliza solamente durante la validación.
        NO modifica los nombres originales del DataFrame.
        """

        nombre = str(nombre).strip()

        # En Fase 2 se utilizó "tipo_".
        # En Fase 3 decidimos utilizar "propiedad_".
        if nombre.startswith("propiedad_"):
            nombre = nombre.replace(
                "propiedad_",
                "tipo_",
                1
            )

        # Solo normalizamos las variables creadas
        # mediante One-Hot Encoding.
        prefijos_categoricos = (
            "comuna_",
            "tipo_",
            "habitacion_"
        )

        if nombre.startswith(prefijos_categoricos):

            # Reemplazar "/" por "_"
            nombre = nombre.replace("/", "_")

            # Reemplazar espacios u otros caracteres
            # por guion bajo.
            nombre = re.sub(
                r"[^0-9A-Za-zÁÉÍÓÚáéíóúÑñ_]+",
                "_",
                nombre
            )

            # Evitar guiones bajos repetidos.
            nombre = re.sub(
                r"_+",
                "_",
                nombre
            )

            nombre = nombre.strip("_")

        return nombre


    def comparar_con_fase2(
        self,
        df_fase2,
        tolerancia=1e-10
    ):
        """
        Compara el resultado del pipeline de Fase 3
        con el conjunto procesado obtenido en Fase 2.

        Los nombres de las variables categóricas se normalizan
        únicamente para realizar la comparación, ya que en Fase 3
        se decidió utilizar una nomenclatura más uniforme.

        Los DataFrames originales no son modificados.
        """

        # --------------------------------------------------
        # 1. Verificar que Fase 2 sea un DataFrame
        # --------------------------------------------------

        if not isinstance(df_fase2, pd.DataFrame):
            raise TypeError(
                "El conjunto de Fase 2 debe ser un DataFrame de pandas."
            )


        # --------------------------------------------------
        # 2. Comparar dimensiones
        # --------------------------------------------------

        assert self.df.shape == df_fase2.shape, (
            "Las dimensiones son diferentes.\n"
            f"Fase 3: {self.df.shape}\n"
            f"Fase 2: {df_fase2.shape}"
        )

        print(
            "✓ Las dimensiones coinciden:",
            self.df.shape
        )


        # --------------------------------------------------
        # 3. Crear copias para comparar
        # --------------------------------------------------

        df_f3_comparacion = self.df.copy()
        df_f2_comparacion = df_fase2.copy()


        # --------------------------------------------------
        # 4. Normalizar nombres de columnas
        # --------------------------------------------------

        df_f3_comparacion.columns = [
            self._normalizar_nombre_columna(c)
            for c in df_f3_comparacion.columns
        ]

        df_f2_comparacion.columns = [
            self._normalizar_nombre_columna(c)
            for c in df_f2_comparacion.columns
        ]


        # --------------------------------------------------
        # 5. Revisar que la normalización no genere
        #    nombres duplicados
        # --------------------------------------------------

        duplicadas_f3 = (
            df_f3_comparacion.columns[
                df_f3_comparacion.columns.duplicated()
            ]
            .tolist()
        )

        duplicadas_f2 = (
            df_f2_comparacion.columns[
                df_f2_comparacion.columns.duplicated()
            ]
            .tolist()
        )

        assert not duplicadas_f3, (
            "La normalización generó columnas duplicadas "
            f"en Fase 3: {duplicadas_f3}"
        )

        assert not duplicadas_f2, (
            "La normalización generó columnas duplicadas "
            f"en Fase 2: {duplicadas_f2}"
        )


        # --------------------------------------------------
        # 6. Comparar conjunto de columnas
        # --------------------------------------------------

        columnas_f3 = set(
            df_f3_comparacion.columns
        )

        columnas_f2 = set(
            df_f2_comparacion.columns
        )

        faltantes = sorted(
            columnas_f2 - columnas_f3
        )

        adicionales = sorted(
            columnas_f3 - columnas_f2
        )

        assert columnas_f3 == columnas_f2, (
            "Las variables de Fase 2 y Fase 3 "
            "no son equivalentes.\n"
            f"Faltantes en Fase 3: {faltantes}\n"
            f"Adicionales en Fase 3: {adicionales}"
        )

        print(
            "✓ Las variables de Fase 2 y Fase 3 "
            "son equivalentes."
        )


        # --------------------------------------------------
        # 7. Ordenar columnas de la misma manera
        # --------------------------------------------------

        columnas_ordenadas = sorted(
            df_f2_comparacion.columns
        )

        df_f2_comparacion = (
            df_f2_comparacion[
                columnas_ordenadas
            ]
            .reset_index(drop=True)
        )

        df_f3_comparacion = (
            df_f3_comparacion[
                columnas_ordenadas
            ]
            .reset_index(drop=True)
        )


        # --------------------------------------------------
        # 8. Comparar los valores
        # --------------------------------------------------

        pd.testing.assert_frame_equal(
            df_f3_comparacion,
            df_f2_comparacion,
            check_dtype=False,
            check_exact=False,
            rtol=tolerancia,
            atol=tolerancia
        )

        print(
            "✓ Los valores procesados coinciden "
            "con los obtenidos en Fase 2."
        )

        print(
            "✓ La reorganización del código mediante POO "
            "no alteró el resultado del procesamiento."
        )

        return True


