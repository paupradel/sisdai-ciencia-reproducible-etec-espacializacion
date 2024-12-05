import numpy as np
import pandas as pd
import geopandas as gpd
from tkinter import filedialog
import os
from tabulate import tabulate

'''Módulo para cargar y analizar diferentes tipos de archivos geoespaciales y tabulares.'''

def info__capa(capa):
    '''Muestra información detallada sobre una capa de datos con formato mejorado.

    Esta función imprime:
    - Dimensiones de la tabla.
    - Nombres de los campos.
    - Tipos de datos de los campos (formateados en una tabla).

    Parámetros:
    ----------
    capa : DataFrame o GeoDataFrame
        La tabla o capa que se desea analizar.

    Ejemplo:
    --------
    info__capa(capa)
    '''
    print("Resumen de la capa:\n")
    print(f"Dimensiones de la tabla --> Filas: {capa.shape[0]}, Columnas: {capa.shape[1]}\n")
    
    print("Nombres de los campos -->")
    print(", ".join(capa.columns))
    print("\nTipos de datos en los campos:")
    
    # Crear una tabla para tipos de datos
    tipos_datos = [(col, str(dtype)) for col, dtype in zip(capa.columns, capa.dtypes)]
    print(tabulate(tipos_datos, headers=["Campo", "Tipo de Dato"], tablefmt="pretty"))

def cargar_capa_geoespacial():
    '''Carga una capa desde un archivo geoespacial (GPKG, Shapefile, GeoJSON, etc.).

    Al ejecutar esta función:
    1. Se abrirá una ventana para seleccionar un archivo geoespacial.
    2. La capa seleccionada se cargará como un GeoDataFrame.
    3. Se imprimirá información sobre la capa cargada.

    Formatos soportados:
    --------------------
    - GeoPackage (.gpkg)
    - Shapefile (.shp)
    - GeoJSON (.geojson)
    - Otros formatos compatibles con GeoPandas.

    Retorna:
    --------
    GeoDataFrame
        La capa cargada desde el archivo seleccionado.

    Ejemplo:
    --------
    capa = modulos.importar.cargar_capa_geoespacial()
    '''
    diractual = os.getcwd()
    ruta = filedialog.askopenfilename(initialdir=os.path.join("..", "datos"),
                                      title="Abrir archivo geoespacial",
                                      filetypes=(("Archivos geoespaciales", "*.gpkg;*.shp;*.geojson"), 
                                                 ("Todos los archivos", "*.*")))
    capa = gpd.read_file(ruta)
    print("Archivo: \n", ruta, "\n")
    info__capa(capa)
    print('\nMarco de referencia para sistemas de coordenadas --> ', capa.crs)   
    return capa

def cargar_excel(campos=None):
    '''Carga una tabla desde un archivo Excel (.xlsx).

    Al ejecutar esta función:
    1. Se abrirá una ventana para seleccionar un archivo .xlsx.
    2. La tabla seleccionada se cargará como un DataFrame.
    3. Se imprimirá información sobre la tabla cargada.

    Parámetros:
    ----------
    campos : dict, opcional
        Un diccionario que especifica los tipos de datos para las columnas 
        del archivo Excel. Si no se proporciona, se usarán los tipos predeterminados.

    Retorna:
    --------
    DataFrame
        La tabla cargada desde el archivo .xlsx.

    Ejemplo:
    --------
    capa = modulos.importar.xlsx()
    capa = modulos.importar.xlsx(campos={'columna1': str, 'columna2': int})
    '''
    diractual = os.getcwd()
    ruta = filedialog.askopenfilename(initialdir=os.path.join("..", "datos"),
                                      title="Abrir solo archivos .xlsx",
                                      filetypes=(("xlsx files", "*.xlsx*"), 
                                                 ("all files", "*.*")))
    capa = pd.read_excel(ruta, sheet_name=0, dtype=campos)
    info__capa(capa)
    return capa

def cargar_csv(campos=None):
    '''Carga una tabla desde un archivo CSV (.csv).

    Al ejecutar esta función:
    1. Se abrirá una ventana para seleccionar un archivo .csv.
    2. La tabla seleccionada se cargará como un DataFrame.
    3. Se imprimirá información sobre la tabla cargada.

    Parámetros:
    ----------
    campos : dict, opcional
        Un diccionario que especifica los tipos de datos para las columnas 
        del archivo CSV. Si no se proporciona, se usarán los tipos predeterminados.

    Retorna:
    --------
    DataFrame
        La tabla cargada desde el archivo .csv.

    Ejemplo:
    --------
    capa = modulos.importar.csv()
    capa = modulos.importar.csv(campos={'columna1': str, 'columna2': float})
    '''
    diractual = os.getcwd()
    ruta = filedialog.askopenfilename(initialdir=os.path.join("..", "datos"),
                                      title="Abrir solo archivos .csv",
                                      filetypes=(("csv files", "*.csv*"), 
                                                 ("all files", "*.*")))
    capa = pd.read_csv(ruta, encoding='ISO-8859-1', dtype=campos)
    info__capa(capa)
    return capa