# Preprocesamientos para capas de información geoespacial

## 📋 Resumen
Este proyecto proporciona un conjunto de herramientas para preprocesar capas de información geoespacial, siguiendo la [metodología ETEC](https://cdn.conahcyt.mx/gema/documentos/Procesos_ETEC-2024_V3.pdf) (Estructuración y Transformación, Espacialización y Carga) del Proyecto GEMA.

## 📖 Introducción

El proyecto tiene como objetivo principal ofrecer herramientas de preprocesamiento para la manipulación y análisis de datos geoespaciales. Aunque no siempre obligatorios, estos preprocesamientos son frecuentemente requeridos dentro del marco de la metodología ETEC. Su aplicación no es secuencial, ya que depende del tipo de datos, su formato y su origen.

## 🚀 Cómo usar la aplicación

Para utilizar las herramientas de procesamiento incluidas en este proyecto, se recomienda configurar un entorno virtual con las bibliotecas necesarias. Sigue los pasos detallados en los cuadernos (notebooks) que encontrarás en la ruta `sisdai-etec-espacializacion/procesamiento/python/cuadernos` en donde se encuentran ejemplos aplicados para realizar los preprocesamientos según tus necesidades de análisis y procesamiento de datos geoespaciales.

Abre los cuadernos de trabajo que necesites y ejecuta las celdas de código según sea necesario.

#### Cuaderno de trabajo: `01_carga_tus_archivos.ipynb`

Este cuaderno te guiará en el proceso de carga de tus archivos geoespaciales, ya sea en formato `Geopackage (.gpkg)`, `Excel (.xlsx)` o `Comma Separeted Values (.csv)`.

#### Cuaderno de trabajo: `02_limpieza_estructura_ejemA.ipynb`

Este cuadernos te guiará en el proceso de limpieza, estructuración y espacialización de datos geoespaciales. Se trata de un ejemplo con datos de presas en México en el cual te guiamos para aplicar algunas de la funciones disponibles en los módulos de preprocesamiento. Como resultado final, obtendrás un archivo geoespacial en formato `Geopackage (.gpkg)`.



## 📦 Estructura de archivos


```plaintext
SISDAI-ETEC-ESPACIALIZACION/
├── datos/
│   ├── datos-auxiliares/
│   ├── datos-originales/
│   ├── datos-procesados/
│   │   └── .gitkeep
├── procesamiento/
│   ├── python/
│   │   ├── cuadernos/
│   │   └── modulos/
│   │       └── generador_metadatos/
│   │       └── preprocesos_capas/
│   │           ├── __init__.py
│   │           ├── importar.py
│   │           ├── procesos.py
│   │           ├── README.md
│   │       └── .gitkeep

```

## 📜 Licencia

SOFTWARE LIBRE Y ESTÁNDARES ABIERTOS

Sisdai está alineado a las disposiciones establecidas por la Coordinación de Estrategia Digital Nacional (DOF: 06/09/2021) en donde se estipula que las "políticas y disposiciones tienen como objetivo fortalecer el uso del software libre y los estándares abiertos, fomentar el desarrollo de aplicaciones institucionales con utilidad pública, lograr la autonomía, soberanía e independencia tecnológicas dentro de la APF". En el artículo 63 se explicita que "cuando se trate de desarrollos basados en software libre, se respetarán las condiciones de su licenciamiento original [...]", en este sentido este proyecto está alineado a lo que se define desde [SALSA.](https://salsa.crip.conacyt.mx/)