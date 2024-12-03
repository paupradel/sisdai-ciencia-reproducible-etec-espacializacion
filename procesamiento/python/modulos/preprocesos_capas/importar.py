import os
import io
import geopandas as gpd
import pandas as pd
import ipywidgets as widgets
from IPython.display import display, HTML

def info_capa(capa):

    '''Función que da información sobre una capa o tabla'''
    
    print('\nDimensiones de la tabla --> ', capa.shape)
    print('\nNombres de los campos --> ', list(capa))
    print('\nTipos de dato en los campos:\n', capa.dtypes) 

def seleccionar_archivo(tipo_archivo):

    '''Función que permite seleccionar y cargar un archivo según el tipo especificado'''

    if tipo_archivo == "gpkg":
        uploader = widgets.FileUpload(accept='.gpkg', multiple=False)
    elif tipo_archivo == "xlsx":
        uploader = widgets.FileUpload(accept='.xlsx', multiple=False)
    elif tipo_archivo == "csv":
        uploader = widgets.FileUpload(accept='.csv', multiple=False)
    else:
        display(HTML('<span style="color:red; font-weight:bold;">⚠️ Tipo de archivo no soportado.</span>'))
        return None
    
    display(uploader)
    return uploader

def cargar_capa(uploader, tipo_archivo):

    '''Función para cargar y mostrar información de archivos .gpkg, .xlsx, o .csv después de ser subidos'''
    
    if uploader and len(uploader.value) > 0:
        for item in uploader.value:
            content = item['content']
            if tipo_archivo == "gpkg":
                with io.BytesIO(content) as f:
                    capa = gpd.read_file(f)
                    display(HTML('<span style="color:green; font-weight:bold;"> Archivo cargado exitosamente 🌱 .</span>'))
                    display(HTML('<span style="color:gray; font-weight:bold;"> #----------- Información de la capa 🌎 -----------#  .</span>'))
                    print('Marco de referencia para sistemas de coordenadas --> ', capa.crs)
                    info_capa(capa)
                    return capa
            elif tipo_archivo == "xlsx":
                with io.BytesIO(content) as f:
                    capa = pd.read_excel(f, sheet_name=0)
                    display(HTML('<span style="color:green; font-weight:bold;"> Archivo cargado exitosamente 🌱 .</span>'))
                    display(HTML('<span style="color:gray; font-weight:bold;"> #----------- Información de la tabla 📊 -----------#  .</span>'))
                    info_capa(capa)
                    return capa
            elif tipo_archivo == "csv":
                with io.BytesIO(content) as f:
                    capa = pd.read_csv(f)
                    display(HTML('<span style="color:green; font-weight:bold;"> Archivo cargado exitosamente 🌱 .</span>'))
                    display(HTML('<span style="color:gray; font-weight:bold;"> #----------- Información de la tabla 📊 -----------#  .</span>'))
                    info_capa(capa)
                    return capa
    else:
        display(HTML('<span style="color:red; font-weight:bold;">⚠️ No se ha cargado ningún archivo.</span>'))
        return None
    
