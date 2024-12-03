import numpy as np
import pandas as pd
import geopandas as gpd
from tkinter import filedialog
import os

'''Documentación del módulo'''

def info__capa(capa):
    '''Función que da info sobre una capa'''
    print('Dimensiones de la tabla --> ', capa.shape)
    print('\nNombres de los campos --> ', list(capa))
    print('\nTipos de dato en los campos:\n', capa.dtypes) 

def gpkg():
    '''Función que importa capas gpkg, al llamar esta función
    se despliega una ventana en donde hay que seleccionar el archivo
    gpkg, se da click en aceptar y se cargará la capa en un 
    geodataframe, ejemplo:
    capa = modulos.importar.gpkg()'''
    diractual = os.getcwd()
    ruta = filedialog.askopenfilename(initialdir = diractual,
                                        title = "Abrir solo archivos .gpkg",
                                        filetypes=(("GPKG files", "*.gpkg*"), 
                                                ("all files", "*.*")))
    capa = gpd.read_file(ruta)
    print("Archivo: \n", ruta, "\n")
    info__capa(capa)
    print('\nMarco de referencia para sistemas de coordenadas --> ', capa.crs)   
    return(capa)

def excel(campos=None):
    """Función que carga una tabla xlsx y da información sobre el contenido,
    al llamar la función se despliega una ventana en donde hay que seleccionar
    el archivo xlsx,ejemplo:
    capa = modulos.importar.xlsx()"""
    diractual = os.getcwd()
    ruta = filedialog.askopenfilename(initialdir = diractual,
                                        title = "Abrir solo archivos .xlsx",
                                        filetypes=(("xlsx files", "*.xlsx*"), 
                                                ("all files", "*.*")))
    capa = pd.read_excel(ruta, sheet_name=0, dtype=campos )
    info__capa(capa)
    return(capa)

def csv(campos=None): # Si no se manda el tipo de columas, no se toma en cuenta el dtype al abrir el csv.
    """Función que carga una tabla csv y da información sobre el contenido,
    al llamar la función se despliega una ventana en donde hay que seleccionar
    el archivo csv,ejemplo:
    capa = modulos.importar.csv()"""
    diractual = os.getcwd()
    ruta = filedialog.askopenfilename(initialdir = diractual,
                                        title = "Abrir solo archivos .csv",
                                        filetypes=(("csv files", "*.csv*"), 
                                                ("all files", "*.*")))
    capa = pd.read_csv(ruta, encoding='ISO-8859-1', dtype=campos)
    info__capa(capa)
    return(capa)