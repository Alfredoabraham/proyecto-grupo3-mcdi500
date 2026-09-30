---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.19.5
kernelspec:
  name: grupo3_mcdi500
  display_name: Python (grupo3.mcdi500)
  language: python
---

# Trazabilidad de mejoras

+++

#### descripción: 
El documento changelo.md describe los feedbaks que se recibieron a lo largo  del proyecto con sus respectivas fechas y las acciones que se tomaron para mejorarlo.

#### justificación: 

changelog.md se creo con el objetivo de documentar la trazabilidad de las mejoras y las acciones adoptadas para dichas mejoras, que se realizaron a lo largo de las fases del proyecto.

+++

| Fecha | Observación formativa | Acción de mejora | Evidencia para verificarla |
|---|---|---|---|
|22/09/2026| Circulan distintas versiones de la pregunta de investigación; el mapa presenta seis preguntas sin acotar. | Acordar una sola pregunta que pueda responderse con Inside Airbnb y escribirla igual en el informe, README y notebook. Dejar las demás como secundarias. | Pregunta idéntica en los tres archivos y mapa corregido. |
|22/09/2026| Se afirma sin fuente que no ajustar precios por temporada reduce los ingresos. | Presentar esa afirmación como hipótesis, no como hecho comprobado. | Redacción corregida en el informe. |
|22/09/2026| El README conserva marcas de conflicto y hay dos versiones del notebook de F2. | Resolver el conflicto, conservar un solo notebook y ejecutarlo completo. | README limpio y notebook único con resultados visibles. |
|22/09/2026| El código sigue en celdas sueltas; el informe describe lo que se haría, no lo realizado. | Trasladar el código a `src`, comenzando por la función de carga. Reescribir el informe en pasado con cifras de filas, faltantes y tratamientos aplicados. | Carpeta `src` e informe concordante con el notebook ejecutado. |
|16/09/2026| La reflexión técnica describe actividades, pero no justifica decisiones ni explicita supuestos, alcance y pendientes. | Explicar por qué se eligieron las herramientas, qué supuestos se adoptan, qué queda fuera del alcance y qué decisiones siguen abiertas. | Sección de reflexión técnica revisada. |
|16/09/2026| El entorno técnico está incompleto. | Incorporar `.gitignore`, establecer la convención de prefijos para commits y documentar el entorno virtual reconstruible con `requirements.txt`. | Archivos, instrucciones e historial del repositorio. |
|16/09/2026| Ninguno de los diagramas incluye leyenda; el segundo usa comandos como conectores y contiene imprecisiones. | Añadir leyenda a ambos diagramas. Corregir e integrar el segundo con conectores que expresen relaciones, o retirarlo. | Mapa y diagramas corregidos en el entregable. |
|16/09/2026| El conjunto tiene 90 variables y 18.534 registros; se anticipan faltantes, desbalance y valores extremos. | Seleccionar mediante código las variables pertinentes, documentar el filtro, comparar tratamientos de preprocesamiento y medir su efecto sobre la dispersión. | Código, resultados y decisiones documentadas en notebook e informe. |
|16/09/2026| Se requiere un historial de trabajo identificable por integrante. | Verificar que los cuatro integrantes puedan hacer *push*, repartir tareas por archivo, trabajar en ramas propias y revisar antes de integrar. | Historial de commits y revisiones por integrante. |

```{code-cell} ipython3

```
