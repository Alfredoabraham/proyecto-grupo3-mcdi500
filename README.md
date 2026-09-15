# Proyecto Grupo 3 — MCDI500

Breve descripción de la problemática abordada y del objetivo del análisis
(2 o 3 frases).

## Integrantes- Rolando Donoso (@rdonosoguerra94)- Nombre Apellido (@usuario-github)

## Datos

Fuente del conjunto, licencia o condiciones de uso, número de registros y
variables. Si el conjunto no está versionado: dónde descargarlo y en qué
carpeta colocarlo.

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

