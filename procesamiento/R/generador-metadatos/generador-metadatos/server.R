library(shiny)
library(sf)
library(readr)

options(shiny.maxRequestSize = 800 * 1024^2)  # Define el peso maximo de los archivos

server <- function(input, output, session) {
  
  # Definiciones predeterminadas para variables comunes
  descripciones_predefinidas <- list(
    g_id = "identificador único consecutivo",
    cve_ent = "clave INEGI de la entidad federativa",
    nom_ent = "nombre de la entidad federativa",
    cve_mun = "clave INEGI del municipio",
    nom_mun = "nombre del municipio",
    cvegeomun = "clave INEGI concatenada de la entidad federativa y el municipio",
    cve_loc = "clave INEGI de la localidad",
    nom_loc = "nombre de la localidad",
    cvegeoloc = "clave INEGI concatenada de la entidad federativa, municipio y localidad",
    cve_ageb = "clave INEGI del Área Geoestadística Básica",
    cvegeoageb = "clave INEGI concatenada de la entidad federativa, municipio, localidad y AGEB",
    cv_mz = "clave INEGI de la manzana",
    cvegeomz = "clave INEGI concatenada de la entidad federativa, municipio, localidad AGEB y manzana",
    cve_cp = "clave del código postal",
    x_long = "coordenada de longitud en formato decimal",
    y_lat = "coordenada de latitud en formato decimal"
  )
  
  # Lectura de informacion del archivo cargado. "reacciona/es reactivo" a la carga
  info_archivo <- reactive({
    req(input$gpkg_file)
    file_path <- input$gpkg_file$datapath
    file_name <- tools::file_path_sans_ext(basename(input$gpkg_file$name))  # lee el nombre sin la extension
    dir_path <- dirname(file_path)  # ruta del archivo
    
    file_ext <- tools::file_ext(file_path)
    
    if(file_ext == "csv") {
      dat <- tryCatch({ read_csv(file_path) }, error = function(e) { NULL })
      tipo <- "csv"
      extension <- "no aplica"
      sist_ref <- "no aplica"
    } else if (file_ext == "gpkg") {
      dat <-  tryCatch({ st_read(file_path, quiet = TRUE) }, error = function(e) { NULL })
      tipo <- "gpkg"
      bb <- st_bbox(dat)
      extension <- paste0("(", bb["xmin"], bb["xmax"], bb["ymin"], bb["ymax"], ")")
      sist_ref <- paste("EPSG:", st_crs(dat)$epsg)
    } 
    
    detalles <- paste0("el conjunto de datos cuenta con ", ncol(dat), " campos y ", nrow(dat), " registros")
    
    list(data = dat,
         tamano = round(file.size(file_path)/(1024*1024), 3),
         name = file_name,
         path = dir_path,
         tipo = tipo,
         extension = extension,
         detalles = detalles,
         sist_ref = sist_ref
    )
  })

  
  # Genera campos de entrada dinamicos para cada campo en el conjunto de datos
  output$entradas_diccionario <- renderUI({
    req(info_archivo()$data)
    
    campos <- names(info_archivo()$data)
    input_list <- lapply(campos, function(campo) {
      # Revisa si hay una descripcion predefinida para el campo
      texto_predeterm <- descripciones_predefinidas[[campo]] %||% ""
      
      textInput(inputId = paste0("desc_", campo), 
                label = paste("Descripción para", campo),
                value = texto_predeterm,  # Descripcion predefinida (si existe)
                placeholder = "Ingresa la descripción")
    })
    
    do.call(tagList, input_list)
  })
  
  # Reactivo: genera el txt final con base en el texto predefinido y la informacion ingresada por la usuaria
  texto_final <- reactive({
    req(info_archivo()$data)
    campos <- names(info_archivo()$data)
    
    # Texto predefinido con indicadores de informacion a ingresar
    plantilla_texto <- paste0(
      "Metadato estructurado conforme a la Norma Técnica Mexicana para la Elaboración de Metadatos Geográficos", 
      "\n",
      "\n",
      "* SECCIÓN 1. Identificación del conjunto de datos espaciales o producto",
      "\n",
      "* SUBSECCIÓN 1.1. Identificación del conjunto de datos espaciales o producto",
      "\n",
      "- Ecosistema Nacional Informático (ENI): ", input$eni, ".\n",
      "- Capítulo ENI: ", input$capitulo, ".\n",
      "- Subcapítulo ENI: ", input$subcapitulo, ".\n",
      "- Título del conjunto de datos espaciales o producto: ", input$titulo, ".\n",
      "- Descripción del conjunto de datos espaciales o producto: ", input$descripcion, ".\n",
      "- Nombre de archivo: ", info_archivo()$name, ".\n",
      "\n",
      "* SUBSECCIÓN 1.2. Enfoque específico del conjunto de datos o producto",
      "\n",
      "- Propósito y uso específico: ", input$proposito, ".\n",
      "- Tema principal del conjunto de datos espaciales o producto: ", input$tema_principal, ".\n",
      "- Grupo de datos del conjunto de datos espaciales o producto: ", input$grupo, ".\n",
      "- Palabras clave: ", input$palabras_clave, ".\n",
      "\n",
      "* SUBSECCIÓN 1.3. Parámetros del conjunto de datos o producto",
      "\n",
      "- Idioma del conjunto de datos espaciales o producto: ", input$idioma, ".\n",
      "- Forma de presentación de los datos espaciales: ", input$presentacion, ".\n",
      "- URL del recurso: ", input$url_recurso, ".\n",
      "- Frecuencia de mantenimiento y actualización: ", input$mantenimiento, ".\n",
      "- Codificación: ", input$codificacion, ".\n",
      "- Estructura de datos: ", input$estructura, ".\n",
      "- Tipo de geometría: ", input$tipo_geometria, ".\n",
      "- Tamaño de archivo: ", info_archivo()$tamano, " Mb.\n",
      "- Formato: ", info_archivo()$tipo, ".\n",
      "\n",
      "\n",
      "* SECCIÓN 2. Fechas relacionadas con el conjunto de datos espaciales o productos",
      "\n",
      "- Fecha de referencia del conjunto de datos espaciales o producto: ", input$fecha_referencia, ".\n",
      "- Tipo de fecha: ", input$tipo_fecha, ".\n",
      "- Fecha de creación de los insumos: ", input$fecha_creacion, ".\n",
      "- Nombre del insumo: ", input$nombre_insumo, ".\n",
      "\n",
      "\n",
      "* SECCIÓN 3. Unidad del estado responsable del conjunto de datos espaciales o productos",
      "\n",
      "- Nombre de la organización: ", input$nombre_organizacion, ".\n",
      "- Enlace en línea: ", input$enlace_linea, ".\n",
      "\n",
      "\n",
      "* SECCIÓN 4. Localización geográfica del conjunto de datos espaciales o productos",
      "\n",
      "- Coordenadas máximas y mínimas: ", info_archivo()$extension, ".\n",
      "\n",
      "\n",
      "* SECCIÓN 5. Sistema de referencia",
      "\n",
      "- Unidades de coordenadas: ", input$unidades_coord, ".\n",
      "- Sistema de referencia de coordenadas: ", info_archivo()$sist_ref, ".\n",
      "\n",
      "\n",
      "* SECCIÓN 6. Calidad de la información (linaje)",
      "\n",
      "- Linaje: ", input$linaje, ".\n",
      "- Pasos del proceso: ", input$pasos, ".\n",
      "- Responsable de la estructuración del conjunto de datos: ", input$responsable, ".\n",
      "- Fuente: ", input$fuente, ".\n",
      "\n",
      "\n",
      "* SECCIÓN 7. Entidades y atributos",
      "\n",
      "- Detalle de entidades y atributos: ", info_archivo()$detalles, ".\n",
      "\n",
      "\n",
      "* SECCIÓN 8. Distribución",
      "\n",
      "- Tipo de licenciamiento: ", input$licenciamiento, ".\n",
      "\n",
      "\n",
      "* SECCIÓN 9. Información del contacto para los metadatos",
      "\n",
      "- Nombre de la organización: ", input$nombre_organizacion, ".\n",
      "- Correo electrónico de contacto: ", input$correo_contacto, ".\n",
      "- Fecha de los metadatos: ", input$fecha_metadatos, ".\n", 
      "\n",
      "\n",
      "################################################################",
      "\n",
      "Notas u observaciones: ", input$notas, ".\n",
      "\n",
      "################################################################",
      "\n",
      "\n",
      "-----------------------------------------------------------------",
      "DICCIONARIO DE CAMPOS O VARIABLES",
      "\n"
    )
    
    # Llena campos de datos con textos predefinidos
    for (campo in campos) {
      descripcion <- input[[paste0("desc_", campo)]] %||% "Sin descripción"
      plantilla_texto <- paste0(plantilla_texto, 
                              "--------------------\n",  # Separador entre campos
                              "campo: ", campo, "\n",
                              "descripción: ", descripcion, "\n")#,
    }
    
    plantilla_texto
  })
  
  # Muestra el texto generado en la interfaz
  output$texto_generado <- renderText({
    texto_final()
  })
  
  # Manejador de descarga para guardar el texto en formato .txt 
  output$guardar_texto <- downloadHandler(
    filename = function() {
      paste0(info_archivo()$path, "/", info_archivo()$name, ".txt")
    },
    content = function(file) {
      writeLines(texto_final(), file)
    }
  )
}
