# Preprocesamientos para capas de información geoespacial

![Estatus](https://img.shields.io/badge/Estatus-desarrollo-yellow)

Este proyecto ofrece un conjunto de preprocesamientos esenciales para capas de información geoespacial, alineados con la metodología de los [procesos ETEC](https://cdn.conahcyt.mx/gema/documentos/Proceso_ETEC-Desglosado_V2.pdf) (Estructuración y Transformación, Espacialización y Carga) del Proyecto de Investigación GEMA.

## Introducción / Acerca de este proyecto

El objetivo principal es proporcionar herramientas de preprocesamiento que, aunque no siempre obligatorias, son comúnmente necesarias dentro del marco de la metodología ETEC. Estos preprocesamientos no siguen un flujo lineal, sino que su aplicación depende de la naturaleza de los datos, el formato en el que se presentan y la fuente de información.  

La sección de procesamiento está dividida en dos apartados diferentes. Existe una carpeta de `python` que incluye herramientas desarrolladas especialmente para llevar a cabo estos procaesos utilizando ese lenguaje de programación, así como ejemplos de uso. Adicionalmente, hay una carpeta de `R` donde ponemos a disposición una serie de ejemplos de cómo utilizar herramientas existentes para llevar a cabo diferentes pasos del proceso ETEC.   


## Requerimientos / Dependencias
### `python`

### `R`

Para correr este procesamiento se requieren las siguientes herramientas
- [R (> 4.0)](https://www.r-project.org/)
- [Quarto](https://quarto.org/) 
- Paquete [sf](https://r-spatial.github.io/sf/), utilizado para manipulación de información espacial
- Paquete [dplyr](https://dplyr.tidyverse.org/), para manipulación de datos
- Paquete [tidyr](https://tidyr.tidyverse.org/), para limpieza y organización de datos  
- Paquete [here](https://here.r-lib.org/), para simplificar el proceso de utilizar rutas relativas

Adicionalmente te recomendamos contar con los siguientes paquetes:
- [ggplot2](https://ggplot2.tidyverse.org/) para visualización de datos
- [readr](https://readr.tidyverse.org/) para lectura de archivos de texto
- [janitor](https://cran.r-project.org/web/packages/janitor/vignettes/janitor.html) para limpieza de datos 
- [stringr](https://stringr.tidyverse.org/) para manipulación de texto.

También recomendamos instalar el IDE [Rstudio](https://www.rstudio.com/categories/rstudio-ide/), sin embargo es posible correr este proyecto con cualquier otro IDE donde puedas utilizar `R`.  

## Estructura del repositorio
```
/espacializacion
├── README
├── datos
│   ├── datos-auxiliares
│   ├── datos-originales
│   └── datos-procesados
├── procesamiento
│   ├── python
│   │   ├── cuadernos
│   │   └── modulos
│   └── R
└── .gitignore
```

## Instrucciones
### Genral
Para algunos de los ejemplos que presentamos aquí, utilizamos capas descargadas desde el [portal de Gema](gema.conahcyt.mx). Por conveniencia, en la carpeta de `datos/datos_auxiliares` de este repositorio incluimos las capas de división estatal (la cual se generó con base en el marco geoestadístico del INEGI 2020) y la división municipal  (la cual se generó con base en el marco geoestadístico del INEGI 2023). Recuerda que en Gema puedes encontrar más de 500 capas de información geográfica para complementar tus análisis.

### `python`

### `R`
En el apartado de `R` encontrarás ejemplos en formato quarto que puedes seguir para elaborar diferentes tipos de capas según los datos con los que cuentes.

