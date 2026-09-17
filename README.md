# Proyecto Grupo 3 — MCDI500

Buscamos determinar qué cracateristicas observables  de los anuncios están relacionadas con las diferencias de valor y precio. El objetivo es analizar las caracteristicas de los alojamientos publicados , que presntena relacion con el precio por noche publicado , utilizando variables disponibles en el dataset y  tecnicas reporduccibles de analisis de datos. La pregunta que abarca la problematica a nuestro proyecto es:

¿De qué manera las características del alojamiento, como ubicación, especificaciones y las cualidades del anfitrión se relacionan con el precio por noche listado en Airbnb en Santiago?


<<<<<<< HEAD
## Integrantes- Rolando Donoso (@rdonosoguerra94)- Alfredo Abraham (@Alfredoabraham)
=======
## Integrantes- Rolando Donoso (@rdonosoguerra94) - Alfredo Abraham (@Alfredoabraham) - Felipe Gutiérrez Castro (@Felipe-I-GC)- Christian Vasquez (@cristian2779cucho)
>>>>>>> 4d50ff0d412e30f37ea03b86bca38f69ae870d97

## Datos

### Fuente y descripción del conjunto de datos

El conjunto de datos utilizado en este proyecto corresponde a alojamientos de **Airbnb en Santiago de Chile**. Los datos fueron obtenidos desde **Inside Airbnb**, plataforma que proporciona datos públicos sobre alojamientos de Airbnb para distintas ciudades del mundo.

### Fuente

- **Fuente:** Inside Airbnb
- **Ciudad:** Santiago, Chile
- **Archivo:** `listings.csv.gz`
- **Formato:** CSV comprimido en GZIP
- **Página de descarga:** [Inside Airbnb – Get the Data](https://insideairbnb.com/es/get-the-data/)
- **Licencia:** Creative Commons Attribution 4.0 International (CC BY 4.0)

### Características del conjunto de datos

El conjunto de datos utilizado contiene:

- **Registros:** 18.534
- **Variables:** 90

Las variables contienen información relacionada con los alojamientos, anfitriones, ubicación, características de las propiedades, precios, disponibilidad y evaluaciones, entre otros atributos.

### Descarga y almacenamiento

El conjunto de datos no se encuentra versionado dentro del repositorio mediante Git. Para reproducir el análisis, el archivo puede descargarse desde la página oficial de Inside Airbnb:

[Inside Airbnb – Get the Data](https://insideairbnb.com/es/get-the-data/)

Una vez descargado, el archivo debe ubicarse en:

data/raw/listings.csv.gz

## Estructura del repositorio

### Estructura general del repositorio

F1/  Definición del problema y entorno reproducible
F2/  Obtención, limpieza y transformación de datos
F3/  Núcleo algorítmico: programación estructurada, recursiva y POO
F4/  Análisis, visualización y comunicación de resultados

proyecto-grupo3-mcdi500/
├─ data/raw/          datos originales, inmutables
├─ data/processed/    resultado del preprocesamiento
├─ notebooks/         análisis documentado por fase
├─ src/               funciones reutilizables
├─ docs/              documentación y referencias
├─ requirements.txt   dependencias con versiones declaradas
├─ .gitignore         qué queda fuera del control de versiones
└─ README.md          descripción del proyecto y forma de reproducirlo

### Estructura especifica repositorio:

proyecto-grupo3-mcdi500/
├─ data/
│ ├─ raw/ # Dataset original, sin modificar
│ └─ processed/ # Datos limpios y transformados
├─ F1/
│ └─ F1\_Definicion.ipynb #notebook donde se definira la problemática
├─ F2/
│ └─ F2\_Procesamiento.ipynb #notebook donde se procesarán los datos
├─ src/ # Funciones reutilizables del pipeline
├─ docs/ # Diccionario de datos, referencias y decisiones
├─ README.md # Descripción e instrucciones para ejecutar
├─ requirements.txt # Dependencias y versiones
├─ .gitignore # Archivos que no se suben
└─ .venv/ # Entorno virtual local — no versionar

## Requisitos y ejecución

Python 3.13
python -m venv .venv
source .venv/Scripts/activate

# Windows, Git Bash

# .venv\\Scripts\\Activate.ps1     # Windows, PowerShell

# source .venv/bin/activate      # macOS y Linux

python -m pip install -r requirements.txt
Ejecutar los notebooks en orden desde la raíz del proyecto.

## Convención de commits

Prefijos usados: docs, data, feat, fix.

## Decisiones técnicas

Registro breve de las decisiones relevantes y su motivo.
Ejemplo: "Se imputa la edad con la mediana en lugar de eliminar registros,
porque los NA representan el 12% de la muestra y su eliminación sesgaría
la distribución por región."

