# Proyecto Grupo 3 — MCDI500

Buscamos determinar qué caracteristicas observables  de los anuncios de Airbnb , están relacionadas con las diferencias de valor y precio. El objetivo es analizar las caracteristicas de los alojamientos publicados , que presntena relacion con el precio por noche publicado , utilizando variables disponibles en el dataset y  tecnicas reporduccibles de analisis de datos. La pregunta que abarca la problematica a nuestro proyecto es:

¿Que caracteristicas observables de los alojamientos ( ubicacion , anfitrion , comuna ,etc.)se relacionan con las diferencias de precio?.


## Integrantes- Rolando Donoso (@rdonosoguerra94) - Alfredo Abraham (@Alfredoabraham) - Felipe Gutiérrez Castro (@Felipe-I-GC)- Christian Vasquez (@cristian2779cucho)


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

```text
F1/  Definición del problema y entorno reproducible
F2/  Obtención, limpieza y transformación de datos
F3/  Núcleo algorítmico: programación estructurada, recursiva y POO
F4/  Análisis, visualización y comunicación de resultados
```

### Dentro de la carpeta SRC se creo un archivo temporal , con el objeto de que la estructura definida sea mostrada en el repositorio , cabe mencionar,  que sin este archivo temporal el .gitignore ignora la carpeta src. 

### Estructura especifica repositorio:
```text
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
```
## Requisitos y ejecución

Python 3.13
python -m venv .venv
source .venv/Scripts/activate

Windows, Git Bash

.venv\\Scripts\\Activate.ps1     # Windows, PowerShell

source .venv/bin/activate      # macOS y Linux

python -m pip install -r requirements.txt
Ejecutar los notebooks en orden desde la raíz del proyecto.

## Convención de commits

- `docs` → documentación
- `data` → datos
- `feat` → nuevas funcionalidades/análisis
- `fix` → correcciones
- `chore` → mantenimiento/configuración

| Tipo | Ejemplo Commits | Explicación |
|---|---|---|
| `docs` | `docs: agrega README y definición del problema` | Documenta el proyecto y define el problema de investigación. |
| `data` | `data: incorpora dataset original en data/raw` | Incorpora el conjunto de datos original en la carpeta `data/raw`. |
| `feat` | `feat: crea notebook F1 de definición del proyecto` | Incorpora el notebook correspondiente a la definición del proyecto. |
| `feat` | `feat: implementa exploración inicial de variables` | Realiza una exploración inicial de las variables del conjunto de datos. |
| `fix` | `fix: corrige tratamiento de valores faltantes` | Corrige el tratamiento de los valores faltantes durante la preparación de los datos. |
| `chore` | `chore: configura entorno y dependencias del proyecto` | Configura elementos técnicos del proyecto, como el entorno virtual y las dependencias. |

## Decisiones técnicas
Decisiones técnicas

Durante el desarrollo de la Fase 2 se adoptaron decisiones técnicas orientadas a garantizar un proceso de análisis reproducible, trazable y coherente con la problemática definida en la Fase 1.

En primer lugar, se utilizó Python como lenguaje principal de programación y Jupyter Notebook como entorno de trabajo, debido a que permiten integrar código, resultados, visualizaciones y documentación narrativa dentro de un mismo flujo de análisis. Para el tratamiento de los datos se emplearon principalmente bibliotecas como pandas y NumPy, mientras que las herramientas de visualización se utilizaron para apoyar la exploración y validación de los resultados.

El conjunto de datos original de Inside Airbnb Santiago se mantuvo sin modificaciones en la carpeta data/raw. Esta decisión permite conservar una fuente de datos original e inalterada y realizar todas las operaciones de limpieza y transformación mediante código, evitando modificaciones manuales que puedan dificultar la reproducción del análisis.

La selección de variables se realizó considerando su relación directa con la pregunta de investigación: ¿Que caracteristicas observables de los alojamientos ( ubicacion , anfitrion , comuna ,etc.)se relacionan con las diferencias de precio? Por esta razón, se priorizaron variables relacionadas con ubicación, tipo de alojamiento, precio, capacidad, disponibilidad y evaluaciones, descartando aquellas que no aportaban directamente al objetivo del estudio.

Durante la etapa de preparación y limpieza de los datos se realizó inicialmente un filtro de variables, seleccionando aquellas que resultaban pertinentes para responder la pregunta de investigación y cumplir con los objetivos definidos. Posteriormente, se efectuó un análisis exploratorio de las variables seleccionadas, revisando su estructura, tipos de datos, distribución, valores nulos, registros duplicados y posibles valores atípicos.

A partir de esta revisión, se llevó a cabo la limpieza de las variables, identificando y tratando datos no válidos, inconsistentes o ausentes según las características de cada variable. En particular, las variables monetarias fueron transformadas a un formato numérico adecuado para facilitar los cálculos, comparaciones y análisis posteriores. Finalmente, las decisiones relacionadas con el filtrado, eliminación, conservación o transformación de los datos fueron documentadas con el propósito de mantener la trazabilidad y reproducibilidad del proceso de análisis.

## FASE 3 ##

## Actualización Fase 3 — Programación Orientada a Objetos

Durante la Fase 3 se reorganizó y amplió el procesamiento del proyecto Airbnb Santiago, incorporando conceptos de Programación Orientada a Objetos (POO), modularización, validación y análisis de eficiencia.

### Principales cambios realizados

- Se reorganizó el preprocesamiento mediante una arquitectura basada en **Programación Orientada a Objetos (POO)**.
- Se integraron los módulos desarrollados en la carpeta `src/`, separando las responsabilidades de carga, limpieza, codificación, escalamiento y validación.
- Se implementó un **pipeline de transformación**, permitiendo ejecutar secuencialmente las distintas etapas del procesamiento.
- Se incorporó el patrón **Strategy** para comparar diferentes estrategias de escalamiento.
- Se compararon `StandardScaler` y `RobustScaler`, manteniendo `RobustScaler` como estrategia utilizada en el pipeline.
- Se conservó una copia interpretable de los datos (`df_analisis`) antes de aplicar One-Hot Encoding, permitiendo mantener variables categóricas como comuna, tipo de propiedad y tipo de habitación.
- Se mantuvo sin escalar la variable objetivo `price_quote_price_per_night`.
- Se incorporó **One-Hot Encoding** para las variables categóricas utilizadas por el modelo de transformación.
- Se normalizaron nombres de variables generadas durante el proceso de codificación.
- Se incorporó una clase de **validación** para comprobar la integridad del dataset transformado.
- Se comparó el resultado de Fase 3 con el dataset procesado generado durante la Fase 2.
- Se agregaron pruebas de casos límite y manejo de excepciones:
  - entrada que no corresponde a un DataFrame;
  - DataFrame vacío;
  - presencia de valores nulos;
  - detección de modificaciones respecto del dataset de referencia.
- Se agregaron verificaciones mediante `assert` para comprobar la ausencia de valores nulos y la conservación de la variable de precio.
- Se incorporó una visualización mediante **boxplot** para verificar el comportamiento de las variables numéricas escaladas.
- Se mantuvo la vinculación del procesamiento con la pregunta del proyecto mediante análisis del **precio por comuna y tipo de habitación**.
- Se incorporó un ejemplo de **herencia**, comparando estrategias de limpieza mediante una clase base y una clase especializada.
- Se aplicó **recursividad** para transformar metadatos anidados del pipeline en una estructura tabular.
- Se incorporó la generación y exportación de `metadatos_pipeline_f3.csv`.
- Se comparó la eficiencia entre un **bucle tradicional** y una **operación vectorizada con pandas/NumPy**, utilizando mediciones de tiempo y memoria.
- Se incorporó la exportación opcional del dataset final transformado como:

  `Data/Processed/airbnb_f3_poo_transformado.csv`

- Se agregó documentación narrativa en Markdown para explicar cada etapa del notebook.
- Se incorporaron citas dentro del desarrollo y una sección final de **Bibliografía en formato APA 7**.

Por lo tanto, la arquitectura que está utilizando actualmente F3 es:
```text
proyecto-grupo3-mcdi500/
│
├── Data/
│   ├── Raw/
│   │   └── listings.csv.gz
│   │
│   └── Processed/
│       ├── airbnb_procesado.csv
│       └── airbnb_f3_poo_transformado.csv
│
├── F1/
│
├── F2/
│
├── F3/
│   └── notebooks/
│       └── F3_S02_POO_Airbnb_Grupo3.ipynb
│
├── src/
│   ├── carga.py
│   ├── limpieza.py
│   ├── transformacion.py
│   └── validacion.py
│
├── docs/
│   └── metadatos_pipeline_f3.csv
│
└── README.md
```
## FASE 4

### Consolidación, optimización, validación y comunicación del proyecto

La **Fase 4** corresponde a la etapa final de integración del proyecto **Airbnb Santiago**. En esta fase se consolidan los desarrollos realizados durante F1, F2 y F3, manteniendo la trazabilidad desde la definición de la problemática y preparación de los datos hasta el desarrollo algorítmico, validación, análisis y comunicación de los resultados.

El notebook principal de esta fase integra los módulos desarrollados en la carpeta `src/`, permitiendo reutilizar las funciones y clases implementadas previamente para mantener una arquitectura modular, reproducible y de fácil mantenimiento.

El flujo general consolidado considera:

```text
Definición del problema
        ↓
Carga de datos
        ↓
Exploración
        ↓
Limpieza
        ↓
Transformación
        ↓
Validación
        ↓
Desarrollo algorítmico
        ↓
Evaluación de eficiencia
        ↓
Análisis de datos
        ↓
Visualización de resultados
        ↓
Interpretación y conclusiones
```

### Objetivo de la Fase 4

El objetivo de esta fase es consolidar una solución reproducible que permita analizar las características observables de los alojamientos Airbnb y determinar cuáles presentan relación con las diferencias de precio por noche en Santiago.

La pregunta que orienta el análisis continúa siendo:

> **¿Qué características observables de los alojamientos (ubicación, anfitrión, comuna, tipo de alojamiento, entre otras) se relacionan con las diferencias de precio?**

### Integración de las fases F1–F4

La Fase 4 consolida el trabajo desarrollado progresivamente durante el proyecto:

- **F1 – Definición:** formulación de la problemática, pregunta de investigación, objetivos y configuración inicial del entorno reproducible.
- **F2 – Preprocesamiento:** exploración, selección, limpieza, transformación y validación inicial de los datos.
- **F3 – Desarrollo algorítmico:** incorporación de programación estructurada, recursividad, Programación Orientada a Objetos, modularización y evaluación de eficiencia.
- **F4 – Consolidación:** integración del pipeline, validación final, optimización, análisis, visualización e interpretación de resultados.

De esta forma, cada fase constituye una evolución de la anterior y permite mantener la trazabilidad de las decisiones técnicas realizadas durante el desarrollo.

### Arquitectura modular

La Fase 4 reutiliza los módulos desarrollados por el equipo en la carpeta `src/`:

```text
src/
├── carga.py
├── limpieza.py
├── transformacion.py
└── validacion.py
```

Cada módulo posee una responsabilidad específica dentro del procesamiento:

- `carga.py`: carga y lectura de los datos utilizados por el proyecto.
- `limpieza.py`: procedimientos y clases relacionados con limpieza y preparación de los registros.
- `transformacion.py`: transformación, codificación y escalamiento de las variables.
- `validacion.py`: comprobaciones destinadas a verificar la integridad y consistencia de los datos procesados.

Esta separación permite reducir la duplicación de código y facilita la reutilización, mantenimiento y extensión del proyecto.

### Validación técnica

Durante la consolidación se realizan verificaciones destinadas a comprobar el correcto funcionamiento del pipeline y la calidad de los datos resultantes.

Entre las validaciones consideradas se encuentran:

- comprobación de valores nulos;
- verificación de tipos y estructuras de datos;
- comprobación de variables requeridas;
- validación de resultados intermedios;
- conservación de variables relevantes para el análisis;
- manejo de entradas incorrectas y excepciones;
- comparación con resultados obtenidos en fases anteriores.

Estas comprobaciones permiten detectar inconsistencias antes de realizar los análisis y visualizaciones finales.

### Eficiencia y optimización

El proyecto incorpora mediciones de rendimiento para comparar diferentes formas de resolver operaciones sobre los datos.

Se consideran comparaciones entre implementaciones tradicionales y operaciones vectorizadas utilizando herramientas del ecosistema Python. Las mediciones permiten analizar tiempos de ejecución y justificar técnicamente la selección de las alternativas utilizadas en el pipeline final.

La optimización no se limita únicamente a reducir tiempos de ejecución, sino también a mantener un código legible, modular, reutilizable y escalable.

### Visualización y análisis de resultados

La Fase 4 incorpora visualizaciones analíticas orientadas a identificar patrones y relaciones entre las características de los alojamientos y el precio publicado por noche.

Las visualizaciones finales permiten estudiar principalmente:

1. **Precio según comuna:** permite comparar las diferencias de precio observadas entre distintas comunas de Santiago e identificar patrones asociados a la ubicación.

2. **Precio según tipo de alojamiento o habitación:** permite analizar cómo las características y modalidad del alojamiento se relacionan con las diferencias observadas en el precio.

3. **Relación entre características del alojamiento y precio:** permite evaluar gráficamente variables relevantes seleccionadas durante el análisis y su posible relación con el valor publicado por noche.

Las visualizaciones son desarrolladas utilizando **Matplotlib y Seaborn** y consideran:

- títulos descriptivos;
- identificación de ejes;
- unidades y escalas adecuadas;
- leyendas cuando corresponde;
- identificación de la fuente de los datos;
- presentación clara de los resultados;
- interpretación analítica vinculada con los objetivos del proyecto.

Cada gráfico es acompañado por una interpretación de los patrones observados, permitiendo utilizar las visualizaciones como evidencia para responder la pregunta principal del proyecto.

### Resultados y comunicación

Los resultados obtenidos durante esta fase son analizados considerando los objetivos definidos inicialmente.

La interpretación no se limita a identificar diferencias numéricas, sino que busca establecer qué características observables presentan patrones relevantes respecto del precio de los alojamientos.

Los resultados obtenidos mediante el procesamiento y las visualizaciones constituyen la base para desarrollar la discusión y las conclusiones finales del proyecto, considerando también las limitaciones de los datos y del análisis realizado.

### Reproducibilidad

Para garantizar la reproducibilidad del proyecto se mantiene una estructura organizada del repositorio y un registro de las dependencias necesarias para ejecutar los notebooks.

El entorno puede ser preparado mediante:

```bash
python -m venv .venv
```

En Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instalación de dependencias:

```bash
python -m pip install -r requirements.txt
```

Posteriormente se puede iniciar JupyterLab:

```bash
jupyter lab
```

Los notebooks deben ejecutarse respetando la progresión:

```text
F1 → F2 → F3 → F4
```

### Notebook consolidado F4

El notebook correspondiente a la fase final se encuentra organizado en:

```text
F4/
└── notebooks/
    └── F4_Consolidado_Proyecto_Airbnb_Grupo3.ipynb
```

Este notebook constituye la integración final del proyecto y reúne el flujo necesario para ejecutar, validar, analizar y comunicar los resultados obtenidos.

### Estructura consolidada del proyecto

```text
proyecto-grupo3-mcdi500/
│
├── Data/
│   ├── Raw/
│   │   └── listings.csv.gz
│   │
│   └── Processed/
│       ├── airbnb_procesado.csv
│       └── airbnb_f3_poo_transformado.csv
│
├── F1/
│   └── notebooks/
│
├── F2/
│   └── notebooks/
│
├── F3/
│   └── notebooks/
│       └── F3_S02_POO_Airbnb_Grupo3.ipynb
│
├── F4/
│   └── notebooks/
│       └── F4_Consolidado_Proyecto_Airbnb_Grupo3.ipynb
│
├── src/
│   ├── carga.py
│   ├── limpieza.py
│   ├── transformacion.py
│   └── validacion.py
│
├── docs/
│   └── metadatos_pipeline_f3.csv
│
├── requirements.txt
├── changelog.md
├── .gitignore
└── README.md
```

### Control de versiones y trazabilidad

Git y GitHub se utilizan para mantener un registro trazable de la evolución del proyecto. Los cambios realizados durante las distintas fases se documentan mediante commits descriptivos asociados a las funcionalidades, correcciones y mejoras incorporadas.

La evolución entre F1, F2, F3 y F4 se complementa mediante el archivo:

```text
changelog.md
```

En este archivo se registran las principales mejoras realizadas, incluyendo fecha, descripción del cambio, commit asociado y justificación técnica.

### Resultado final de la Fase 4

La Fase 4 consolida el proyecto en un flujo completo y reproducible:

**Datos originales → preprocesamiento → transformación → validación → desarrollo algorítmico → evaluación de eficiencia → análisis → visualización → interpretación de resultados.**

Esta integración permite mantener coherencia entre la problemática planteada, las decisiones técnicas adoptadas, el procesamiento realizado y los resultados obtenidos, dejando una estructura documentada y reproducible dentro del repositorio GitHub.
