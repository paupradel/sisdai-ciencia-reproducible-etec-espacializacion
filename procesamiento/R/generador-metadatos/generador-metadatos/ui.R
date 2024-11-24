library(shiny)
library(bslib)

ui <- page_fillable(
  titlePanel("Generador de metadatos"),
  
  p("En esta aplicación puedes generar los metadatos para datos espaciales según los lineamientos establecidos en los procesos ETEC"),
  p("Para empezar, carga una capa o conjunto de datos en formato csv"),
  
  layout_columns(
    

    card(card_header("Información general"),
         p("Aquí están los datos generales del conjunto de datos"),
         fileInput("gpkg_file", "Carga un geopaquete (.gpkg) o archivo csv", 
                   accept = c(".gpkg", ".csv"),
                   buttonLabel = "Explorar...",
                   placeholder = "No se ha seleccionado ningún archivo"
                   ),
         
         # Campos de entrada
         selectInput("eni", "Ecosistema Nacional Informático (ENI)", 
                     choices = c("Agentes Tóxicos y Agentes Contaminantes", 
                                 "Agua", 
                                 "Cultura", 
                                 "Educación",
                                 "Energía y Cambio Climático",
                                 "Salud",
                                 "Seguridad Humana",
                                 "Sistemas Socioecológicos",
                                 "Soberanía Alimentaria", 
                                 "Vivienda",
                                 "no aplica")),
         textInput("capitulo", "Capítulo ENI", value = "no aplica"),
         textInput("subcapitulo", "Subcapítulo ENI", value = "no aplica"),
         textInput("creditos", "Créditos del capítulo o subcapítulo ENI", value = "no aplica"),
         textInput("titulo", "Título del conjunto de datos espaciales o producto"),
         textInput("proposito", "Propósito y uso específico"),
         textInput("descripcion", "Descripción del conjunto de datos espaciales o producto"),
         textInput("idioma", "Idioma del conjunto de datos espaciales o producto", value = "Español"),
         selectInput("tema_principal", "Tema principal del conjunto de datos espaciales o producto*", 
                     choices = c("agricultura",
                                 "biodiversidad",
                                 "atmósfera climatológica",
                                 "economía",
                                 "medio ambiente",
                                 "información geocientífica",
                                 "salud",
                                 "base de imágenes de mapas de la cobertura de la tierra",
                                 "inteligencia militar",
                                 "aguas interiores",
                                 "localización",
                                 "planeamiento catastral",
                                "sociedad",
                                 "estructura",
                                 "transportación",
                                 "comunicación de servicios"
                     )),
         selectInput("grupo", "Grupo de datos del conjunto de datos espaciales o producto:", 
                     choices = c("recursos naturales y clima",
                                 "nombres geográficos",
                                 "catastrales",
                                 "topográficos",
                                 "relieve continental",
                                 "límites costeros",
                                 "marco de referencia geodésico"
                     )),
         textInput("palabras_clave", "Palabras clave"),
         textInput("presentacion", "Forma de presentación de los datos espaciales", 
                   value = "mapa digital"),
         textInput("url_recurso", "URL del recurso"),
         selectInput("mantenimiento", "Frecuencia de mantenimiento y actualización", 
                     choices = c(
                       "no programado",
                       "diariamente",
                       "semanalmente",
                       "quincenalmente",
                       "mensualmente",
                       "trimestralmente",
                       "semestralmente",
                       "anualmente",
                       "irregularmente",
                       "desconocido",
                       "otro"
                     )),
         textInput("codificacion", "Codificación", 
                   value = "UTF-8"),
         selectInput("estructura", "Estructura de datos",
                     choices = c("vectorial", "raster")),
         selectInput("tipo_geometria", "Tipo de geometría",
                     choices = c("polígonos (a)", "líneas (l)", "puntos (p)")),
         textInput("fecha_referencia", "Fecha de referencia de los datos espaciales o producto"),
         selectInput("tipo_fecha", "Frecuencia de mantenimiento y actualización", 
                     choices = c(
                       "creación - indicador de la fecha que especifica cuándo fue creado el recurso",
                       "publicación - indicador de la fecha que especifica cuándo el recurso fue publicado",
                       "revisión - identificador de la fecha que especifica cuándo el recurso fue examinado o reexaminado y mejorado o corregido"
                     )),
         textInput("fecha_creacion", "Fecha de craeci[on de los insumos"),
         textInput("nombre_insumo", "Nombre del insumo"),
         textInput("nombre_organizacion", "Nombre de la organización"),
         textInput("enlace_linea", "Enlace en línea"),
         textInput("unidades_coord", "Unidades de coordenada", value = "grados decimales"),
         textInput("linaje", "Linaje"),
         textInput("pasos", "Pasos del proceso"),
         textInput("responsable", "Responsable de la estructuración del conjunto de datos"),
         textInput("fuente", "Fuente"),
         selectInput("licenciamiento", "Tipo de licenciamiento",
                     choices = c("bajo los términos de libre uso MX de los Datos Abiertos del gobierno de México, ver https://datos.gob.mx/libreusomx", 
                                 "copyright (derechos de autor)", 
                                 "patente", 
                                 "pendiente de patentar",
                                 "marca registrada", 
                                 "licencia", 
                                 "derechos de propiedad intelectual",
                                 "restringido", 
                                 "otras restricciones-limitaciones no listadas")),
         textInput("correo_contacto", "Correo electrónico de contacto"),
         textInput("fecha_metadatos", "Fecha de los metadatos"),
         textInput("notas", "Notas u observaciones", value = "no aplica"),
        
         
         p("* Las opciones mostradas están basadas en las temáticas establecidas en la Norma
Técnica Mexicana para la Elaboración de Metadatos Geográficos
(https://www.inegi.org.mx/contenidos/infraestructura/datos/doc/Norma_Tecnica_para
_la_elaboracion_de_Metadatos_Geograficos.pdf).")

    ),

card(card_header("Diccionario de datos"),
     p("Por favor completa la información acerca de las variables del conjunto"),
     uiOutput("entradas_diccionario"),  # Marcador de posicion para campos dinamicos
),

card(card_header("Metadatos"), 
     p("Aquí puedes ir viendo cómo quedará tu archivo de metadatos"),
     verbatimTextOutput("texto_generado"),  # Muestra el texto final con lo ingresado por la usuaria
     
     downloadButton("guardar_texto", "Guardar metadatos (.txt)")  # Boton para guardar metadatos en formato .txt
),
col_widths = c(3, 3, 6)
  )

)
