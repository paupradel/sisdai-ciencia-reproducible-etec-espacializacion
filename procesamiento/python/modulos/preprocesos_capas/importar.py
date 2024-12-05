import numpy as np
import pandas as pd
import geopandas as gpd
from tkinter import filedialog
import os

'''Módulo para cargar y analizar diferentes tipos de archivos geoespaciales y tabulares.'''

def info__capa(capa):
    '''Muestra información detallada sobre una capa de datos.

    Esta función imprime:
    - Dimensiones de la tabla.
    - Nombres de los campos.
    - Tipos de datos de los campos.

    Parámetros:
    ----------
    capa : DataFrame o GeoDataFrame
        La tabla o capa que se desea analizar.

    Ejemplo:
    --------
    info__capa(capa)
    '''
    print('Dimensiones de la tabla --> ', capa.shape)
    print('\nNombres de los campos --> ', list(capa))
    print('\nTipos de dato en los campos:\n', capa.dtypes)

def gpkg():
    '''Carga una capa desde un archivo GeoPackage (.gpkg).

    Al ejecutar esta función:
    1. Se abrirá una ventana para seleccionar un archivo .gpkg.
    2. La capa seleccionada se cargará como un GeoDataFrame.
    3. Se imprimirá información sobre la capa cargada.

    Retorna:
    --------
    GeoDataFrame
        La capa cargada desde el archivo .gpkg.

    Ejemplo:
    --------
    capa = modulos.importar.gpkg()
    '''
    diractual = os.getcwd()
    ruta = filedialog.askopenfilename(initialdir=diractual,
                                      title="Abrir solo archivos .gpkg",
                                      filetypes=(("GPKG files", "*.gpkg*"), 
                                                 ("all files", "*.*")))
    capa = gpd.read_file(ruta)
    print("Archivo: \n", ruta, "\n")
    info__capa(capa)
    print('\nMarco de referencia para sistemas de coordenadas --> ', capa.crs)   
    return capa

def excel(campos=None):
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
    ruta = filedialog.askopenfilename(initialdir=diractual,
                                      title="Abrir solo archivos .xlsx",
                                      filetypes=(("xlsx files", "*.xlsx*"), 
                                                 ("all files", "*.*")))
    capa = pd.read_excel(ruta, sheet_name=0, dtype=campos)
    info__capa(capa)
    return capa

def csv(campos=None):
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
    ruta = filedialog.askopenfilename(initialdir=diractual,
                                      title="Abrir solo archivos .csv",
                                      filetypes=(("csv files", "*.csv*"), 
                                                 ("all files", "*.*")))
    capa = pd.read_csv(ruta, encoding='ISO-8859-1', dtype=campos)
    info__capa(capa)
    return capa