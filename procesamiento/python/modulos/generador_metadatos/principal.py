#-*- coding: utf-8 -*-
"""
--- Aplicación que despliega una interfaz que tiene como finalidad generar fichas de
    metadatos según la Norma Técnica para la elaboración de Metadatos geográficos (NTMG).
    Las salidas que se obtienen son fichas de metadatos por medio de archivos de texto en formato txt.---
"""
###################################################################################

import os
from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askdirectory, askopenfilename
from jinja2 import Environment, FileSystemLoader
import geopandas as gpd
import pandas as pd
from string import Template
from matplotlib import image
from matplotlib.pyplot import text
from osgeo import ogr

##################################################################################
            #### Funciones ####
##################################################################################

def open_file():
    print("\n\n##################################################################################\n\n")
    filename = askopenfilename(initialdir="~",
        title="Choose a file",
        filetypes=(("all files", "*.*"), ("gpkg files", "*.gpkg"))
    )
    global df, registros, sistemaReferencia, formato, nombreArchivo, extent, campos, sizefile, num_campos #, geometria
    print("filename -->", filename)
    sizefile = str(round(os.stat(filename).st_size/1000000, 2)) + " Mb"
    df = gpd.read_file(filename)
    registros = str(len(df))
    sistemaReferencia = str(df.crs)
    sistemaReferencia = sistemaReferencia.upper()
    punto = filename.rfind(".")
    barra = filename.rfind("/")
    nombreArchivo = filename[barra + 1: punto]
    formato = filename[punto + 1:] + " y geojson (complementario csv y xlsx)"
    shapefile = ogr.Open(filename)
    layer = shapefile.GetLayer()
    #geometria = ogr.GeometryTypeToName(layer.GetGeomType())
    extent = str(layer.GetExtent())
    campos = list(df)
    campos.remove("geometry")
    num_campos = str(len(campos))
    print("Registros --> ", registros)
    print("crs --> ", sistemaReferencia)
    print("Formato --> ", formato)
    print("Nombre del archivo --> ", nombreArchivo)
    print("Extent --> ", extent)
    print("Tamaño de Archivo --> ", sizefile)
    print("Número de campos --> ", num_campos)
    print("campos --> ", campos)
    print("\n\n##################################################################################\n\n")

##################################################################################
            # Generar fichas de metadatos txt y html
##################################################################################

def generar_txt():

    pronacE = str(pronace.get()); enI = str(eni.get())
    sub_eni = str(subEni.get())
    titulo_dataset = str(tituloDataset.get())
    propositO = str(proposito.get())
    descripcioN = str(descripcion.get())
    idiomA = str(idioma.get())
    temA = str(tema.get())
    grupO = str(grupo.get())
    palabras_clave = str(palabrasClave.get())
    forma_representacion = str(formaRepresentacion.get())
    urL = str(url.get())
    perioricidaD = str(perioricidad.get())
    #uso_especifico = str(usoEspecifico.get())
    codificacioN = str(codificacion.get())
    estructura_datos = str(estructuraDatos.get())
    tipo_geometria = str(tipoGeometria.get())
    fecha_ref = str(fechaRef.get())
    tipo_fecha = str(tipoFecha.get())
    fecha_generacion = str(fechaGeneracion.get())
    nombre_insumo = str(nombreInsumo.get())
    nombre_organizacion = str(nombreOrganizacion.get())
    enlace_en_linea = str(enlaceEnLinea.get())
    unidadeS = str(unidades.get())
    linajE = str(linaje.get())
    pasos_proceso = str(pasosProceso.get())
    reponsable_estructuracion = str(responsableEstructuracion.get())
    fuentE = str(fuente.get())
    detalle_ent_atrib = "el conjunto de datos cuenta con " + num_campos + " campos y " +  registros + " objetos geográficos"
    tipo_licenciamiento = str(tipoLicenciamiento.get())
    autor_metadato = str(autorMetadato.get())
    email_contacto = str(emailContacto.get())
    fecha_de_metadatos = str(fechaDeMetadatos.get())
    notaS = str(notas.get())
    
    espacio = " "
    espacio2 = "  "
    espacio3 = "\n"
    print("* SECCIÓN 1. Identificación del conjunto de datos espaciales o producto \n\n")

    print("- Ecosistema Nacional Informático (ENI): ", pronacE)
    print("- Capítulo ENI: ", enI)
    print("- Subcapítulo ENI: ", sub_eni)
    print("- Titulo del conjunto de datos espaciales o producto: ", titulo_dataset)
    print("- Nombre de archivo: ", nombreArchivo)
    print("- Propósito: ", propositO)
    print("- Descripción del conjunto de datos espaciales o producto: ", descripcioN)
    print("- Idioma del conjunto de datos espaciales o producto: ", idiomA)
    print("- Tema principal del conjunto de datos espaciales o producto: ", temA)
    print("- Grupo de datos del conjunto de datos espaciales o producto: ", grupO)
    print("- Palabras Clave: ", palabras_clave)
    print("- Forma de presentación de los datos espaciales: ", forma_representacion)
    print("- URL del recurso: ", urL)
    print("- Frecuencia de mantenimiento y actualización: ", perioricidaD)
    #print("- Uso específico: ", uso_especifico)
    print("- Codificación: ", codificacioN)
    print("- Estructura de Datos: ", estructura_datos)
    print("- Tipo de Geometría: ", tipo_geometria)
    print("- Tamaño de Archivo: ", sizefile)
    print("- Formato: ", formato)

    print("\n* SECCIÓN 2. Fechas relacionadas con el conjunto de datos espaciales o productos \n\n")

    print("- Fecha de referencia del conjunto de datos espaciales o producto: ", fecha_ref)
    print("- Tipo de fecha: ", tipo_fecha)
    print("- Fecha de creación de los insumos: ", fecha_generacion)
    print("- Nombre del insumo: ", nombre_insumo)

    print("\n* SECCIÓN 3. Unidad del estado responsable del conjunto de datos espaciales o productos \n\n")

    print("- Nombre de la organización: ", nombre_organizacion)
    print("- Enlace en línea: ", enlace_en_linea)

    print("\n* SECCIÓN 4. Localización geográfica del conjunto de datos espaciales o productos \n\n")

    print("- Capturar Coordenadas Máximas y Mínimas: ", extent)

    print("\n* SECCIÓN 5. Sistema de referencia \n\n")

    print("- Unidades de coordenadas: ", unidadeS)
    print("- Sistema de referencia: ", sistemaReferencia)

    print("\n* SECCIÓN 6. Calidad de la información(Linaje) \n\n")

    print("- Linaje: ", linajE)
    print("- Pasos del proceso: ", pasos_proceso)
    print('- Responsable de la estructuración del conjunto de datos: ', reponsable_estructuracion)
    print("- Fuente: ", fuentE)

    print("\n* SECCIÓN 7. Entidades y atributos \n\n")

    print("- Detalle de entidades y atributos: ", detalle_ent_atrib)

    print("\n* Sección 8. Distribución \n\n")

    print("- Tipo de licenciamiento: ", tipo_licenciamiento)

    print("\n* SECCIÓN 9. Información del contacto para los metadatos \n\n")

    print("- Nombre de la organización: ", autor_metadato)
    print("- Correo electrónico de contacto: ", email_contacto)
    print("- Fecha de los metadatos: ", fecha_de_metadatos)

    print("- Notas u Observaciones: ", notaS)
    print("\n\nMetadato integrado en base a la Norma Técnica Mexicana para la Elaboración de Metadatos Geográficos \n")

    file = askdirectory(parent=ventana, title="select directory")
    file0 = str(file)
    print ("Directorio de salida seleccionado:", file0)
    archivo_txt = "metadato_" + nombreArchivo + ".txt"  
    filein1 = file0 + "/" + archivo_txt
    archivo_html = "metadato_" + nombreArchivo + ".html"
    filein2 = file0 + "/" + archivo_html

    archivo = open(filein1, "w", encoding='utf-8')

    insumos = ['\n\n* SECCIÓN 1. Identificación del conjunto de datos espaciales o producto',
            '* SUBSECCIÓN 1.1. Identificación del conjunto de datos espaciales o producto\n',
            '- Ecosistema Nacional Informático (ENI): ',
            '- Capítulo ENI: ',
            '- Subcapítulo ENI: ',
            '- Título del conjunto de datos espaciales o producto: ',
            '- Descripción del conjunto de datos espaciales o producto: ',
            '- Nombre de archivo: ',
            '* SUBSECCIÓN 1.2. Enfoque específico del conjunto de datos o producto\n',
            '- Propósito y uso específico: ',
            '- Tema principal del conjunto de datos espaciales o producto: ',
            '- Grupo de datos del conjunto de datos espaciales o producto: ',
            '- Palabras clave: ',
            '* SUBSECCIÓN 1.3. Parámetros del conjunto de datos o producto\n',
            '- Idioma del conjunto de datos espaciales o producto: ',
            '- Forma de presentación de los datos espaciales: ',
            '- URL del recurso: ',
            '- Frecuencia de mantenimiento y actualización: ',
            #'- Uso específico: ',
            '- Codificación: ',
            '- Estructura de datos: ',
            '- Tipo de geometría: ',
            '- Tamaño de archivo: ',
            '- Formato: ',
            '\n\n* SECCIÓN 2. Fechas relacionadas con el conjunto de datos espaciales o productos',
            '- Fecha de referencia del conjunto de datos espaciales o producto: ', '- Tipo de fecha: ',
            '- Fecha de creación de los insumos: ', '- Nombre del insumo: ',
            '\n\n* SECCIÓN 3. Unidad del estado responsable del conjunto de datos espaciales o productos',
            '- Nombre de la organización: ', '- Enlace en línea: ',
            '\n\n* SECCIÓN 4. Localización geográfica del conjunto de datos espaciales o productos',
            '- Coordenadas máximas y mínimas: ',
            '\n\n* SECCIÓN 5. Sistema de referencia',
            '- Unidades de coordenadas: ', '- Sistema de referencia de coordenadas: ',
            '\n\n* SECCIÓN 6. Calidad de la información (linaje)',
            '- Linaje: ', '- Pasos del proceso: ', '- Responsable de la estructuración del conjunto de datos: ', '- Fuente: ',
            '\n\n* SECCIÓN 7. Entidades y atributos',
            '- Detalle de entidades y atributos: ',
            '\n\n* SECCIÓN 8. Distribución',
            '- Tipo de licenciamiento: ',
            '\n\n* SECCIÓN 9. Información del contacto para los metadatos',
            '- Nombre de la organización: ', '- Correo electrónico de contacto: ',
            '\n- Fecha de los metadatos: ',
            '\n\n################################################################',
            'Notas u observaciones: ',
            '\n################################################################']
    if notaS == "":
        notaS = "ninguna"
    salidas = [espacio, espacio2, pronacE, enI, sub_eni, titulo_dataset,  descripcioN, nombreArchivo, # Subsección 1.1.
                espacio3, propositO, temA, grupO, palabras_clave,                                     # Subsección 1.2.
                espacio3, idiomA, forma_representacion, urL, perioricidaD, #uso_especifico,           # Subsección 1.3.
                codificacioN, estructura_datos, tipo_geometria, sizefile, formato,                    # Subsección 1.3.
                espacio, fecha_ref, tipo_fecha, fecha_generacion, nombre_insumo,
                espacio, nombre_organizacion, enlace_en_linea, espacio, extent,
                espacio, unidadeS, sistemaReferencia, espacio,linajE, pasos_proceso, reponsable_estructuracion,
                fuentE, espacio, detalle_ent_atrib, espacio, tipo_licenciamiento,
                espacio, autor_metadato, email_contacto, fecha_de_metadatos,
                espacio, notaS, espacio]

    archivo.write("Metadato estructurado conforme a la Norma Técnica Mexicana para la Elaboración de Metadatos Geográficos \n")
    for i in range (len(insumos)):
        if (salidas[i] == espacio):
            #print("------------>> entra a espacio, i --> ", i, 'valor --> ', salidas[i])
            archivo.write(insumos[i] + salidas[i] + "\n\n")
        elif (salidas[i] == espacio2):
            #print("-------------->> entra a espacio2")
            archivo.write(insumos[i])
        elif (salidas[i] == espacio3):
            #print("--------->> entra a espacio3")
            archivo.write(salidas[i] + insumos[i])
        elif (salidas[i] == urL or salidas[i] == enlace_en_linea or salidas[i] == email_contacto or salidas[i] == fuentE or salidas[i] == nombreArchivo or salidas[i] == tipo_licenciamiento or salidas[i] == autor_metadato):
            archivo.write(insumos[i] + salidas[i] + "\n")
        else:
            
            archivo.write(insumos[i] + salidas[i] + "." + "\n") # Checar punto 160522

    print("\n\n--------------------------------------------\nDICCIONARIO DE CAMPOS O VARIABLES")
    archivo.write("--------------------------------------------\nDICCIONARIO DE CAMPOS O VARIABLES\n\n")

    lista = []
    campo_num = "campo"
    for i in range (len(campos)):
        archivo.write('campo:' + " '" + campos[i] + "'" + "\n")
        lista.append(campo_num + str(i+1))
        if(campos[i]=="g_id"):
            lista[i] = "identificador único consecutivo"
            archivo.write("descripción: " + lista[i] + "\n\n")
            print(campos[i], " --> descripción: ", lista[i])
        elif(campos[i]=="cve_ent"):
            lista[i] = "clave INEGI de la entidad federativa"
            archivo.write("descripción: " + lista[i] + "\n\n")
            print(campos[i], " --> descripción: ", lista[i])
        elif(campos[i]=="nom_ent"):
            lista[i] = "nombre de la entidad federativa"
            archivo.write("descripción: " + lista[i] + "\n\n")
            print(campos[i], " --> descripción: ", lista[i])
        elif(campos[i]=="cve_mun"):
            lista[i] = "clave INEGI del municipio"
            archivo.write("descripción: " + lista[i] + "\n\n")
            print(campos[i], " --> descripción: ", lista[i])
        elif(campos[i]=="nom_mun"):
            lista[i] = "nombre del municipio"
            archivo.write("descripción: " + lista[i] + "\n\n")
            print(campos[i], " --> descripción: ", lista[i])
        elif(campos[i]=="cvegeomun"):
            lista[i] = "clave INEGI concatenada de la entidad federativa y el municipio"
            archivo.write("descripción: " + lista[i] + "\n\n")
            print(campos[i], " --> descripción: ", lista[i])
        elif(campos[i]=="cve_loc"):
            lista[i] = "clave INEGI de la localidad"
            archivo.write("descripción: " + lista[i] + "\n\n")
            print(campos[i], " --> descripción: ", lista[i])
        elif(campos[i]=="nom_loc"):
            lista[i] = "nombre de la localidad"
            archivo.write("descripción: " + lista[i] + "\n\n")
            print(campos[i], " --> descripción: ", lista[i])
        elif(campos[i]=="cvegeoloc"):
            lista[i] = "clave INEGI concatenada de la entidad federativa, municipio y localidad"
            archivo.write("descripción: " + lista[i] + "\n\n")
            print(campos[i], " --> descripción: ", lista[i])
        elif(campos[i]=="cve_zm"):
            lista[i] = "clave INEGI de la zona metropolitana"
            archivo.write("descripción: " + lista[i] + "\n\n")
            print(campos[i], " --> descripción: ", lista[i])
        elif(campos[i]=="cvegeozm"):
            lista[i] = "clave concatenada del estado y la zona metropolitana"
            archivo.write("descripción: " + lista[i] + "\n\n")
            print(campos[i], " --> descripción: ", lista[i])
        elif(campos[i]=="nom_zm"):
            lista[i] = "nombres de zonas metropolitanas"
            archivo.write("descripción: " + lista[i] + "\n\n")
            print(campos[i], " --> descripción: ", lista[i])
        elif(campos[i]=="cvegeoageb"):
            lista[i] = "clave INEGI concatenada de la entidad federativa, municipio, localidad y AGEB"
            archivo.write("descripción: " + lista[i] + "\n\n")
            print(campos[i], " --> descripción: ", lista[i])
        elif(campos[i]=="cv_mz"):
            lista[i] = "clave INEGI de la manzana"
            archivo.write("descripción: " + lista[i] + "\n\n")
            print(campos[i], " --> descripción: ", lista[i])
        elif(campos[i]=="cvegeomz"):
            lista[i] = "clave INEGI concatenada de la entidad federativa, municipio, localidad AGEB y manzana"
            archivo.write("descripción: " + lista[i] + "\n\n")
            print(campos[i], " --> descripción: ", lista[i])
        elif(campos[i]=="cve_col"):
            lista[i] = "clave INEGI de la colonia"
            archivo.write("descripción: " + lista[i] + "\n\n")
            print(campos[i], " --> descripción: ", lista[i])
        elif(campos[i]=="nom_col"):
            lista[i] = "nombre de la colonia"
            archivo.write("descripción: " + lista[i] + "\n\n")
            print(campos[i], " --> descripción: ", lista[i])
        elif(campos[i]=="cve_cp"):
            lista[i] = "clave del código postal"
            archivo.write("descripción: " + lista[i] + "\n\n")
            print(campos[i], " --> descripción: ", lista[i])
        elif(campos[i]=="x_long"):
            lista[i] = "coordenada de longitud en formato decimal"
            archivo.write("descripción: " + lista[i] + "\n\n")
            print(campos[i], " --> descripción: ", lista[i])
        elif(campos[i]=="y_lat"):
            lista[i] = "coordenada de latitud en formato decimal"
            archivo.write("descripción: " + lista[i] + "\n\n")
            print(campos[i], " --> descripción: ", lista[i])
        elif(campos[i]=="altitud"):
            lista[i] = "altitud"
            archivo.write("descripción: " + lista[i] + "\n\n")
            print(campos[i], " --> descripción: ", lista[i])
        elif(campos[i]=="area_km"):
            lista[i] = "área calculada en kilómetros cuadrados a partir de la geometría presentada"
            archivo.write("descripción: " + lista[i] + "\n\n")
            print(campos[i], " --> descripción: ", lista[i])
        elif(campos[i]=="area_ha"):
            lista[i] = "área calculada en hectáreas a partir de la geometría presentada"
            archivo.write("descripción: " + lista[i] + "\n\n")
            print(campos[i], " --> descripción: ", lista[i])
        elif(campos[i]=="perim_m"):
            lista[i] = "perímetro calculado en metros a partir de la geometría presentada"
            archivo.write("descripción: " + lista[i] + "\n\n")
            print(campos[i], " --> descripción: ", lista[i])
        elif(campos[i]=="perim_km"):
            lista[i] = "perímetro calculado en kilómetros a partir de la geometría presentada"
            archivo.write("descripción: " + lista[i] + "\n\n")
            print(campos[i], " --> descripción: ", lista[i])
        elif(campos[i]=="longi_m"):
            lista[i] = "longitud calculada en metros a partir de la geometría presentada"
            archivo.write("descripción: " + lista[i] + "\n\n")
            print(campos[i], " --> descripción: ", lista[i])
        elif(campos[i]=="longi_km"):
            lista[i] = "longitud calculada en kilómetros a partir de la geometría presentada"
            archivo.write("descripción: " + lista[i] + "\n\n")
            print(campos[i], " --> descripción: ", lista[i])
        else:
            lista[i] = str(input(campos[i] + " --> descripción: "))
            archivo.write("descripción: " + lista[i] + "\n\n")
            #print(campos[i], " --> descripción: ", lista[i])

    archivo.close()
    print("\n##############################################################")
    print("\n\n        ******************Completado******************\n\n")
    print("##############################################################")
    if (autor_metadato == "Consejo Nacional de Humanidades, Ciencias y Tecnologías.\n\t\t\t\t\t\t\t Coordinación de Repositorios, Investigación y Prospectiva"):
        autor_metadato = 'Consejo Nacional de Humanidades, Ciencias y Tecnologías <br>Coordinación de Repositorios, Investigación y Prospectiva'
    datos = {'campos': campos, 'descr': lista}
    df = pd.DataFrame.from_dict(datos)
    ruta_script = os.getcwd()
    environment = Environment(loader=FileSystemLoader(ruta_script)) # En donde está la plantilla
    results_filename = filein2                                   # Nombre archivo html de salida
    results_template = environment.get_template("template-v2.html") # plantilla
    dic_salidas = {'pronacE': pronacE, 'enI': enI, 'sub_eni': sub_eni, 'titulo_dataset': titulo_dataset,
    'nombreArchivo': nombreArchivo, 'propositO': propositO, 'descripcioN': descripcioN,
    'idiomA': idiomA, 'temA': temA, 'grupO': grupO, 'palabras_clave': palabras_clave,
    'forma_representacion': forma_representacion, 'urL': urL, 'perioricidaD': perioricidaD,
    'codificacioN': codificacioN,
    'estructura_datos': estructura_datos, 'tipo_geometria': tipo_geometria,'sizefile' : sizefile,
    'formato': formato, 'fecha_ref': fecha_ref, 'tipo_fecha': tipo_fecha, 'fecha_generacion': fecha_generacion,
    'nombre_insumo': nombre_insumo, 'nombre_organizacion': nombre_organizacion, 'enlace_en_linea': enlace_en_linea,
    'extent': extent, 'unidadeS': unidadeS, 'sistemaReferencia': sistemaReferencia, 'linajE': linajE,
    'pasos_proceso': pasos_proceso, 'reponsable_estructuracion': reponsable_estructuracion, 'fuentE': fuentE, 'detalle_ent_atrib': detalle_ent_atrib,
    'tipo_licenciamiento': tipo_licenciamiento, 'autor_metadato': autor_metadato, 'email_contacto': email_contacto,
    'fecha_de_metadatos': fecha_de_metadatos, 'notaS': notaS}
    dic_salidas["campos_descr"] = df.to_dict("records")
    with open(results_filename, mode="w", encoding="utf-8") as results:
        results.write(results_template.render(dic_salidas))
        print(f"ヽ(´ー｀)ノ... wrote --> {results_filename}")
    
##################################################################################
            #### Interfaz tk ####
##################################################################################
open_file()  # Se carga la capa
ventana = Tk()

ventana.title("Generador de metadatos")
ventana.geometry("920x695")

#################################################################################
## Declaración de variables ##
##################################################################################

# sección 1. Identificación del conjunto de datos espaciales o producto

pronace = StringVar(); #pronace.set("No aplica") # Combo "Ecosistema Nacional de Investigación (ENI)"
eni = StringVar(); #eni.set("No aplica")         # Combo "Capítulo ENI"
subEni = StringVar(); #subEni.set("No aplica")   # Combo "Subcapítulo ENI"
tituloDataset = StringVar()                  # Título del conjunto de datos espaciales o producto.
#nombreArchivo = StringVar()                 # Automatizado Se anexó
proposito = StringVar()
descripcion = StringVar()                    # Descripción del conjunto de datos espaciales o producto.
idioma = StringVar(); idioma.set("español")  # Idioma del conjunto de datos espaciales o producto.
tema = StringVar()                           # Tema principal del conjunto de datos espaciales o producto. combo
grupo = StringVar()                          # Grupo de datos del conjunto de datos espaciales o producto. combo
palabrasClave = StringVar()
formaRepresentacion = StringVar(); formaRepresentacion.set("mapa digital")  #Forma de presentación de los datos espaciales.
url = StringVar(); url.set("https://gema.conahcyt.mx/") # URL del recurso.
perioricidad = StringVar(); perioricidad.set("no programado")                    # Frecuencia de mantenimiento y actualización. combo
#usoEspecifico = StringVar()                  # Reemplaza uso posible, se fusiona con proposito 110723

codificacion = StringVar(); codificacion.set("UTF-8")                            # Se anexó a la planificación de campos original
estructuraDatos = StringVar()                                                    # SSe anexó a la planificación de campos original
tipoGeometria = StringVar()                                                      # SSe anexó a la planificación de campos original
# numero registros --> automatizada                                              # Se anexó a la planificación de campos original
# tamaño de archivo --> automatizada                                             # Se anexó a la planificación de campos original
# formato --> automatizada                                                       # Se anexó a la planificación de campos original

# Seccion 2. Fechas relacionadas con el conjunto de datos espaciales o productos

fechaRef = StringVar()                       # Fecha de referencia del conjunto de datos espaciales o producto. reemplaza a fechaGeneracion
tipoFecha = StringVar()                      # Combo
fechaGeneracion = StringVar()                # Fecha de creación de los insumos.
nombreInsumo = StringVar()                   # Nombre del insumo.


# Sección 3. Unidad del estado responsable del conjunto de datos espaciales o productos:

nombreOrganizacion =  StringVar(); nombreOrganizacion.set("Consejo Nacional de Humanidades, Ciencias y Tecnologías (Conahcyt)")            # Nombre de la organización. * Autoría de datos fuente
enlaceEnLinea = StringVar(); enlaceEnLinea.set("https://conahcyt.mx/")                  # Enlace en linea, URL de datos fuente

# Sección 4. Localización geográfica del conjunto de datos espaciales o productos:

# Extención --> extent, está automatizada    # Capturar Coordenadas Máximas y Mínimas.

# Sección 5, Sistema de referencia:

unidades = StringVar(); unidades.set("grados decimales")  # Capturar en Coordenadas Geográficas: Resoluciónes: 1,  Unidades de Coordenadas:  Grados, Minutos, Segundos
# Sistema referencia --> sistemaReferencia, está automatizada

# Sección 6.  Calidad de la información(Linaje):

linaje = StringVar();                       # Enunciado (Ejemplo: los datos se tomaron de la Secretaría de Comunicaciones y Transportes)
pasosProceso = StringVar()                  # Ejemplo (Se descargaron los datos, se filtraron por municipio, se intersectaron capas, etc.)
responsableEstructuracion = StringVar()     # Nuevo campo, anexado el 131123
fuente = StringVar()                        # Fuente (https://sct.gob.mx)

# Sección 7. Entidades y atributos

#detalleEntAtrib = StringVar() -->automatizada   # Detalle de entidades y atributos

# Sección 8. Distribución

tipoLicenciamiento = StringVar(); tipoLicenciamiento.set("bajo los términos de libre uso MX de los Datos Abiertos del gobierno de México, ver https://datos.gob.mx/libreusomx") # Se anexó

# Sección 9. Información del contacto para los metadatos

autorMetadato = StringVar(); autorMetadato.set("Consejo Nacional de Humanidades, Ciencias y Tecnologías\n\t\t\t\t\t\t\t Coordinación de Repositorios, Investigación y Prospectiva") # Nombre de la organización
emailContacto = StringVar(); emailContacto.set("dadsig@conahcyt.mx")
fechaDeMetadatos = StringVar()

notas = StringVar();  # Notas u observaciones, se anexó

####################################################################################################

#archivoTxt = StringVar(); archivoTxt.set("archivo.txt") # Nombre de archivo de sálida

####################################################################################################
            ###### Scrollbar ###########
####################################################################################################

# Create a Main frame
main_frame = Frame(ventana)
main_frame.pack(fill=BOTH, expand=1)

# Create a canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Add scrollbar to canvas
the_scrollbar = ttk.Scrollbar(main_frame, orient=VERTICAL, command=my_canvas.yview)
the_scrollbar.pack(side=RIGHT, fill=Y)

# Configure canvas
my_canvas.configure(yscrollcommand=the_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion= my_canvas.bbox('all')))

# Create another frame inside canvas
second_frame = Frame(my_canvas)

# Add that new frame to a window in the canvas
my_canvas.create_window((0,0), window=second_frame, anchor='nw')

###############################################################################
            ###### Etiquetas spinbox y cajas  ###########
###############################################################################

etiqueta0 = Label(second_frame, font=('montserrat', 15),
            text="Generador de metadatos: Proyecto GEMA                                                                              ").grid(row=0, column=2, sticky='E')
#etiqueta1 = Label(second_frame, font=('montserrat', 12, 'bold'),
#            text="sección 1. Identificación del conjunto de datos espaciales o producto               ").grid(row=3, column=0, sticky='E')

etiqueta2 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Ecosistema Nacional Informático (ENI)").grid(row=4, column=0, sticky='E')
combo2 = ttk.Combobox(second_frame, width="60", textvariable=pronace,
        values=("Agentes Tóxicos y Procesos Contaminantes", 
                "Agua", "Cultura", "Educación",
                "Energía y Cambio Climático", "Salud", "Seguridad Humana",
                "Sistemas Socioecológicos", "Soberanía Alimentaria", 
                "Vivienda", "no aplica")).grid(row=4, column=2, sticky='W')

etiqueta3 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Capítulo ENI").grid(row=5, column=0, sticky='E')
combo3 = ttk.Combobox(second_frame, width="60", textvariable=eni,
        values=("Agua y Cuencas en México",
                "Ángelus: personas desaparecidas",
                "Arribo del sargazo a las costas mexicanas",
                "Búsqueda de alternativas al glifosato (Glifosato)",
                "Centros de atención para violencia contra las mujeres en México",
                "Conacyt frente a la Covid-19",
                "Plataforma Nacional Energía, Ambiente y Sociedad (Planeas)",
                "Programa Interinstitucional de Especialidad en Soberanías Alimentarias y Gestión de Incidencia Local Estratégica (PIES-AGILES)",
                "Pueblos y Comunidades Indígenas y Afromexicana",
                "Red de transmisión y vigilancia de farmacorresistencia del VIH en la CDMX",
                "Rescate del Lago de Texcoco",
                "Territorios Tren Maya",
                "Violencia y desigualdades de género",
                "no aplica")).grid(row=5, column=2, sticky='W')

etiqueta3b = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Subcapítulo ENI").grid(row=6, column=0, sticky='E')
combo3b = ttk.Combobox(second_frame, width="60", textvariable=subEni,
        values=("Plataforma para la Planeación Logística de la Campaña Nacional de Vacunación Covid-19",
                "Vigilancia de variantes del virus SARS-CoV-2",
                "Productos de investigación y modelado de datos Covid-19",
                "no aplica")).grid(row=6, column=2, sticky='W')

etiqueta4 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Título del conjunto de datos espaciales o producto").grid(row=7, column=0, sticky='E')
# etiqueta4a = Label(second_frame, font=('montserrat', 10, 'bold'),
#             text="espaciales o producto").grid(row=8, column=0, sticky='E')
tituloCaja4 = Entry(second_frame, textvariable=tituloDataset, 
                    width="60").grid(row=7,column=2, sticky='W')

etiqueta5 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Propósito y uso especifico").grid(row=8, column=0, sticky='E')
tituloCaja5 = Entry(second_frame, textvariable=proposito,
                    width="60").grid(row=8, column=2, sticky='W')

etiqueta6 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Descripción del conjunto de datos espaciales o producto").grid(row=9, column=0, sticky='E')
# etiqueta6a = Label(second_frame, font=('montserrat', 10, 'bold'),
#             text="datos espaciales o producto ").grid(row=11, column=0, sticky='E')
tituloCaja6 = Entry(second_frame, textvariable=descripcion, 
                    width="60").grid(row=9, column=2, sticky='W')

etiqueta7 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Idioma del conjunto de datos espaciales o producto").grid(row=10, column=0, sticky='E')
# etiqueta7a = Label(second_frame, font=('montserrat', 10, 'bold'),
#             text="datos espaciales o producto ").grid(row=13, column=0, sticky='E')
tituloCaja7 = Entry(second_frame, textvariable=idioma,
                    width="60").grid(row=10, column=2, sticky='W')

etiqueta8 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Tema principal del conjunto de datos espaciales o producto").grid(row=12, column=0, sticky='E')
etiqueta8a = Label(second_frame, font=('montserrat', 10, 'bold'), bg="#F9E79F",
            text="Nota: Las opciones mostradas corresponden a las temáticas     ").grid(row=13, column=0, sticky='E')
etiqueta8b = Label(second_frame, font=('montserrat', 10, 'bold'), bg="#F9E79F",
            text="señaladas en la Norma Técnica Mexicana para la Elaboración    ").grid(row=14, column=0, sticky='E')
etiqueta8b = Label(second_frame, font=('montserrat', 10, 'bold'), bg="#F9E79F",
            text="de Metadatos Geográficos y no necesariamente corresponden     ").grid(row=15, column=0, sticky='E')
etiqueta8b = Label(second_frame, font=('montserrat', 10, 'bold'), bg="#F9E79F",
            text="a los temas generales que se indican en la documentación ETEC.").grid(row=16, column=0, sticky='E')
combo8 = ttk.Combobox(second_frame, width="60", textvariable=tema,
        values=("agricultura", "biodiversidad", "atmósfera climatológica", "economía",
        "medio ambiente", "información geocientífica", "salud", "base de imágenes de mapas de la cobertura de la tierra",
        "inteligencia militar", "aguas interiores", "localización", "planeamiento catastral",
        "sociedad", "estructura", "transportación", "comunicación de servicios")).grid(row=16, column=2, sticky='W')

etiqueta9 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Grupo de datos del conjunto de datos espaciales o producto").grid(row=17, column=0, sticky='E')
# etiqueta9a = Label(second_frame, font=('montserrat', 10, 'bold'),
#             text="datos espaciales o producto ").grid(row=20, column=0, sticky='E')
combo9 = ttk.Combobox(second_frame, width="60", textvariable=grupo,
        values=("recursos naturales y clima",
        "nombres geográficos",
        "catastrales",
        "topográficos",
        "relieve continental",
        "límites costeros",
        "marco de referencia geodésico")).grid(row=17, column=2, sticky='W')

etiqueta10 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Palabras Clave ").grid(row=18, column=0, sticky='E')
tituloCaja10 = Entry(second_frame, textvariable=palabrasClave,
                    width="60").grid(row=18, column=2, sticky='W')

etiqueta11 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Forma de presentación de los datos espaciales").grid(row=19, column=0, sticky='E')
# etiqueta11a = Label(second_frame, font=('montserrat', 10, 'bold'),
#             text="los datos espaciales ").grid(row=23, column=0, sticky='E')
tituloCaja11 = Entry(second_frame, textvariable=formaRepresentacion,
                    width="60").grid(row=19, column=2, sticky='W')

etiqueta12 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="URL del recurso ").grid(row=20, column=0, sticky='E')
tituloCaja12 = Entry(second_frame, textvariable=url,
                    width="60").grid(row=20, column=2, sticky='W')

etiqueta13 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Frecuencia de mantenimiento y actualización").grid(row=21, column=0, sticky='E')
# etiqueta13a = Label(second_frame, font=('montserrat', 10, 'bold'),
#             text="y actualización ").grid(row=26, column=0, sticky='E')
combo13 = ttk.Combobox(second_frame, width="60", textvariable=perioricidad,
        values=("diariamente", "semanalmente", "quincenalmente", "mensualmente", "trimestralmente",
        "semestralmente", "anualmente", "irregularmente", "no programado",
        "desconocido", "otro")).grid(row=21, column=2, sticky='W')

# etiqueta14 = Label(second_frame, font=('montserrat', 10, 'bold'),
#             text="Uso específico ").grid(row=22, column=0, sticky='E')
# tituloCaja14 = Entry(second_frame, textvariable=usoEspecifico,
#                     width="60").grid(row=22, column=2, sticky='W')

etiqueta15 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Codificación ").grid(row=22, column=0, sticky='E')
tituloCaja15 = Entry(second_frame, textvariable=codificacion,
                    width="60").grid(row=22, column=2, sticky='W')

etiqueta15 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Estructura de Datos ").grid(row=23, column=0, sticky='E')
combo15 = ttk.Combobox(second_frame, width="60", textvariable=estructuraDatos,
        values=("vectorial", "ráster")).grid(row=23, column=2, sticky='W')

etiqueta16 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Tipo Geometría ").grid(row=24, column=0, sticky='E')
combo16 = ttk.Combobox(second_frame, width="60", textvariable=tipoGeometria,
        values=("polígonos", "líneas", "puntos")).grid(row=24, column=2, sticky='W')

etiqueta17 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Fecha de referencia del conjunto de datos espaciales o producto").grid(row=25, column=0, sticky='E')
# etiqueta17a = Label(second_frame, font=('montserrat', 10, 'bold'),
#             text="de datos espaciales o producto ").grid(row=32, column=0, sticky='E')
tituloCaja17 = Entry(second_frame, textvariable=fechaRef,
                    width="60").grid(row=25, column=2, sticky='W')

etiqueta18 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Tipo Fecha ").grid(row=26, column=0, sticky='E')
combo18 = ttk.Combobox(second_frame, width="60", textvariable=tipoFecha,
        values=("creación - indicador de la fecha que especifica cuándo fue creado el recurso",
        "publicación - indicador de la fecha que especifica cuándo el recurso fue publicado",
        "revisión - identificador de la fecha que especifica cuándo el recurso fue examinado o reexaminado y mejorado o corregido")).grid(row=26, column=2, sticky='W')

etiqueta19 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Fecha de creación de los insumos").grid(row=27, column=0, sticky='E')
# etiqueta19a = Label(second_frame, font=('montserrat', 10, 'bold'),
#             text="de los insumos ").grid(row=35, column=0, sticky='E')
tituloCaja19 = Entry(second_frame, textvariable=fechaGeneracion,
                    width="60").grid(row=27, column=2, sticky='W')

etiqueta20 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Nombre de insumo ").grid(row=28, column=0, sticky='E')
tituloCaja20 = Entry(second_frame, textvariable=nombreInsumo,
                    width="60").grid(row=28, column=2, sticky='W')

etiqueta21 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Nombre de la organización ").grid(row=29, column=0, sticky='E')
tituloCaja21 = Entry(second_frame, textvariable=nombreOrganizacion,
                    width="60").grid(row=29, column=2, sticky='W')

etiqueta22 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Enlace en línea ").grid(row=30, column=0, sticky='E')
tituloCaja22 = Entry(second_frame, textvariable=enlaceEnLinea,
                    width="60").grid(row=30, column=2, sticky='W')

etiqueta23 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Unidades de coordenadas ").grid(row=31, column=0, sticky='E')
tituloCaja23 = Entry(second_frame, textvariable=unidades,
                    width="60").grid(row=31, column=2, sticky='W')

etiqueta24 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Linaje ").grid(row=32, column=0, sticky='E')
tituloCaja24 = Entry(second_frame, textvariable=linaje,
                    width="60").grid(row=32, column=2, sticky='W')

etiqueta25 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Pasos del proceso ").grid(row=33, column=0, sticky='E')
tituloCaja25 = Entry(second_frame, textvariable=pasosProceso,
                    width="60").grid(row=33, column=2, sticky='W')

etiqueta25a = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Responsable de la estructuración del conjunto de datos ").grid(row=34, column=0, sticky='E')
tituloCaja25a = Entry(second_frame, textvariable=responsableEstructuracion,
                    width="60").grid(row=34, column=2, sticky='W')

etiqueta26 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Fuente ").grid(row=35, column=0, sticky='E')
tituloCaja26 = Entry(second_frame, textvariable=fuente,
                    width="60").grid(row=35, column=2, sticky='W')

etiqueta28 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Tipo de licenciamiento ").grid(row=36, column=0, sticky='E')
combo28 = ttk.Combobox(second_frame, width="60", textvariable=tipoLicenciamiento,
        values=("bajo los términos de libre uso MX de los Datos Abiertos del gobierno de México, ver https://datos.gob.mx/libreusomx", 
                "copyright (derechos de autor)", "patente", "pendiente de patentar",
                "marca registrada", "licencia", "derechos de propiedad intelectual",
                "restringido", "otras restricciones-limitaciones no listadas")).grid(row=36, column=2, sticky='W')
# Open Data Commons Open Database License (ODbL)".... osea quedará asi: Tipo de Licenciamiento: Open Data Commons Open Database License (ODbL)
etiqueta29 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Nombre de la organización ").grid(row=37, column=0, sticky='E')
tituloCaja29 = Entry(second_frame, textvariable=autorMetadato,
                    width="60").grid(row=37, column=2, sticky='W')

etiqueta30 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Correo electrónico de contacto ").grid(row=38, column=0, sticky='E')
tituloCaja30 = Entry(second_frame, textvariable=emailContacto,
                    width="60").grid(row=38, column=2, sticky='W')

etiqueta31 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Fecha de los metadatos ").grid(row=39, column=0, sticky='E')
tituloCaja31 = Entry(second_frame, textvariable=fechaDeMetadatos,
                    width="60").grid(row=39, column=2, sticky='W')

etiqueta32 = Label(second_frame, font=('montserrat', 10, 'bold'),
            text="Notas u Observaciones ").grid(row=40, column=0, sticky='E')
tituloCaja32 = Entry(second_frame, textvariable=notas,
                    width="60").grid(row=40, column=2, sticky='W')

###################################################################################
            #### Botones ####
##################################################################################

# Botón de Búsqueda
img_1 = PhotoImage(file="images/browse_img.png")
browse_btn = Button(second_frame, image=img_1, borderwidth=0, command=lambda: open_file())
browse_btn.grid(row=60, column=0, sticky='W', padx=10, pady=5)

etiqueta39 = Label(second_frame, font=('montserrat', 10, 'bold'), text='Búsqueda')
etiqueta39.grid(row=61, column=0, sticky='W', padx=10)

# Botón de Generar
img_2 = PhotoImage(file="images/txt_file1.png")
html_btn = Button(second_frame, image=img_2, borderwidth=0, command=lambda: generar_txt())
html_btn.grid(row=60, column=1, sticky='W', padx=10, pady=5)

etiqueta40 = Label(second_frame, font=('montserrat', 10, 'bold'), text='Genera')
etiqueta40.grid(row=61, column=1, sticky='W', padx=10)

space9 = Label(second_frame, text=" ")
space9.grid(row=62, column=0)

# Botón de Salir
img_3 = PhotoImage(file="images/salida_img.png")
salida_btn = Button(second_frame, image=img_3, borderwidth=0, command=ventana.destroy)
salida_btn.grid(row=60, column=2, sticky='W', padx=10, pady=5)

etiqueta41 = Label(second_frame, font=('montserrat', 10, 'bold'), text='Salir')
etiqueta41.grid(row=61, column=2, sticky='W', padx=10)

##################################################################################

ventana.mainloop()

###############################################################################
            ###### Fin ¯\_(ツ)_/¯ ###########
###############################################################################
