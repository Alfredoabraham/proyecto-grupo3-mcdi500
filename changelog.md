# Trazabilidad de mejoras
    
#### descripción: 
El documento changelog.md describe los feedbaks que se recibieron a lo largo  del proyecto con sus respectivas fechas y las acciones que se tomaron para mejorarlo. Su objetivo es documentar la trazabilidad de las mejoras y las acciones adoptadas para dichas mejoras, que se realizaron a lo largo de las fases del proyecto.


| Fecha de los cambios | Observación formativa | Acción de mejora registrada | Commits relacionados | Justificación |
|---|---|---|---|---|
| 09/09/2026–14/09/2026 | El entorno técnico está incompleto. | Se incorporaron .gitignore y requirements.txt y se actualizaron las dependencias.| `e4e9df6`, `6640e54`| Facilitar la gestión de archivos y la reconstrucción del entorno.|
| 22/09/2026 | Circulan distintas versiones de la pregunta de investigación; el mapa presenta seis preguntas sin acotar. | Se actualizó el README para abordar la coherencia de la pregunta de investigación, según la asociación realizada por el equipo. | `59935e5` | Mantener coherencia entre la pregunta de investigación, las variables seleccionadas y el análisis. |
| 22/09/2026 | El README conserva marcas de conflicto y hay dos versiones del notebook de F2. | Se corrigieron las carpetas repetidas y las rutas incorrectas del notebook F2. | `ae0b49b` | Evitar duplicidades y permitir ejecutar el notebook desde la ubicación definida en el proyecto. |
| 23/09/2026–27/09/2026 | El conjunto tiene 90 variables y 18.534 registros; se anticipan faltantes, desbalance y valores extremos. | Se detalló la selección de variables, se corrigió la estandarización y se añadió una comparación de escaladores. Se incorporaron evaluaciones de eficiencia con distintos tamaños de datos y 100 ejecuciones. | `8da3166`, `7951af2`, `03da2df`, `b6d5d36`, `9c279c7` | Fundamentar la selección y transformación de variables y evaluar el rendimiento del procesamiento. |
| 25/09/2026–27/09/2026 | El código sigue en celdas sueltas; el informe describe lo que se haría, no lo realizado. | Se incorporaron módulos de limpieza, validación, transformación y carga en src/. Se actualizó el README con la arquitectura y los avances de F3. | `36e6540`, `ebb8832`, `b2c60a7`, `d66105f`, `6f44fd5`, `267d250` | Separar responsabilidades, facilitar la reutilización del código y documentar la arquitectura implementada. |
|01/10/2026| Se requiere un historial de trabajo identificable por integrante. |  Se crea archivo .mailmap para robustecer historial de trabajo indetificable por integrante. |`a0d0861`| Evidenciar la colaboración y la integración del trabajo. El commit demuestra que las identidades de los cuatro integrantes están unificadas. |
|03/10/2026| El patrón de diseño no está declarado, y lo tienen implementado. |  Se declara en el notebook f4 |`68b7742`| declarar la comparación de patrones permite apoyar los resultados del notebook |
|03/10/2026|  Tres celdas del notebook de F3 sin ejecutar.| Se eliminan 3 celdas y se ejecuta nuevamente el notebook |`60cc707`| Ejecutar el notebook con contadores continuos |
|03/10/2026| Los datos siguen versionados. El archivo comprimido original más cuatro CSV procesados. declárenlos en el gitignore| se deja solo una version de los datos y se declaran en el .gitignore |`97507c0`, `e5e2999`| Mantener el orden y la limpieza de los datos dentro de la estructura|
|03/10/2026| documenten en el README cómo obtener los datos ignorados.| se añade sección de trazabilidad de datos dentro del README |`9826701`| Mantener el orden y la limpieza de los archivos de datos dentro de la estructura|

