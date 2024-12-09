import pandas as pd
import geopandas as gpd
import numpy as np
from shapely.geometry import Point, LineString, Polygon
from rich.console import Console
from tabulate import tabulate

def info_capa(capa: pd.DataFrame):
    """Proporciona información básica sobre un DataFrame.

    Parámetros:
    capa -- DataFrame del que se proporcionará la información.
    """
    # Validaciones
    assert isinstance(capa, pd.DataFrame), "El parámetro debe ser un DataFrame."

    print('Dimensiones de la tabla --> ', capa.shape)
    print('\nNombres de los campos --> ', list(capa.columns))
    print('\nTipos de dato en los campos:\n', capa.dtypes)

def crea_gid(capa: pd.DataFrame) -> pd.DataFrame:
    """Genera una columna 'g_id' en un DataFrame, eliminando cualquier columna existente con el mismo nombre.

    Parámetros:
    capa -- DataFrame al que se le agregará la columna 'g_id'.

    Retorna:
    capa -- DataFrame con la columna 'g_id' agregada.
    """
    # Validaciones
    assert isinstance(capa, pd.DataFrame), "El parámetro debe ser un DataFrame."

    arreglo = np.arange(1, len(capa) + 1)

    if 'g_id' in capa.columns:
        capa = capa.drop(columns=['g_id'])
    
    capa.insert(0, 'g_id', arreglo)

    return capa

def generar_puntos(capa: pd.DataFrame, c_long: str, c_lat: str) -> gpd.GeoDataFrame:
    """Espacializa un DataFrame con columnas de latitud y longitud, generando una GeoDataFrame de puntos.

    Parámetros:
    capa -- DataFrame a espacializar.
    c_long -- Nombre de la columna de longitud.
    c_lat -- Nombre de la columna de latitud.

    Retorna:
    salida -- GeoDataFrame espacializado con sistema de referencia de coordenadas EPSG:4326.
    """
    # Validaciones
    assert isinstance(capa, pd.DataFrame), "El parámetro 'capa' debe ser un DataFrame."
    assert isinstance(c_long, str), "El nombre de la columna de longitud debe ser una cadena."
    assert isinstance(c_lat, str), "El nombre de la columna de latitud debe ser una cadena."
    assert c_long in capa.columns, f"La columna '{c_long}' no existe en el DataFrame."
    assert c_lat in capa.columns, f"La columna '{c_lat}' no existe en el DataFrame."

    capa = capa.rename(columns={c_long: 'x_long', c_lat: 'y_lat'})

    geometry = [Point(xy) for xy in zip(capa['x_long'], capa['y_lat'])]
    
    salida = gpd.GeoDataFrame(capa, crs="EPSG:4326", geometry=geometry)
    
    info_capa(salida)
    print('\nSistema de referencia de coordenadas (CRS) --> ', salida.crs)
    return salida

def eliminar_columnas(df: pd.DataFrame, cols_a_eliminar: list) -> pd.DataFrame:
    """
    Elimina columnas específicas de un DataFrame.

    Parámetros:
    df -- DataFrame del cual se eliminarán columnas.
    cols_a_eliminar -- Lista con los nombres de las columnas a eliminar.

    Retorna:
    df -- DataFrame sin las columnas especificadas.
    """
    # Validaciones
    assert isinstance(df, pd.DataFrame), "El primer parámetro debe ser un DataFrame."
    assert isinstance(cols_a_eliminar, list), "El segundo parámetro debe ser una lista."
    for col in cols_a_eliminar:
        assert isinstance(col, str), f"Cada nombre de columna en la lista debe ser una cadena. '{col}' no es una cadena."
        assert col in df.columns, f"La columna '{col}' no existe en el DataFrame."

    df.drop(cols_a_eliminar, axis=1, inplace=True)
    return df

def nan_df(df: pd.DataFrame) -> pd.DataFrame:
    """
    Reemplaza los valores nulos de un DataFrame por -999.

    Parámetros:
    df -- DataFrame al que se le reemplazarán los valores nulos.

    Retorna:
    df -- DataFrame con valores nulos reemplazados por -999.
    """

    # Validación
    assert isinstance(df, pd.DataFrame), "El parámetro debe ser un DataFrame."

    df.fillna(-999, inplace=True)
    return df


def nan_columnas(df: pd.DataFrame, dicc: dict) -> pd.DataFrame:
    """
    Reemplaza los valores nulos de columnas específicas en un DataFrame por un valor específico.

    Parámetros:
    df -- DataFrame al que se le reemplazarán los valores nulos.
    dicc -- Diccionario con los nombres de las columnas como claves y los valores a reemplazar como valores.

    Retorna:
    df -- DataFrame con valores nulos reemplazados por el valor especificado en las columnas indicadas.
    
    Ejemplo de uso:
    dicc = {'columna1': -999, 'columna2': -333}
    """

    # Validaciones
    assert isinstance(df, pd.DataFrame), "El primer parámetro debe ser un DataFrame."
    assert isinstance(dicc, dict), "El segundo parámetro debe ser un diccionario."
    
    for col, val in dicc.items():
        assert isinstance(col, str), f"El nombre de columna '{col}' debe ser una cadena."
        assert col in df.columns, f"La columna '{col}' no existe en el DataFrame."
        assert isinstance(val, (int, float, str)), f"El valor de reemplazo para la columna '{col}' debe ser un número o una cadena."
    
    df.fillna(dicc, inplace=True)
    return df

def completar_claves(df: pd.DataFrame, columna: str, n_clave: int) -> pd.DataFrame:
    """
    Completa con ceros a la izquierda los valores de una columna específica en un DataFrame.

    Parámetros:
    df -- DataFrame al que se le completará la columna.
    columna -- Nombre de la columna a completar.
    n_clave -- Número de caracteres que debe tener cada valor en la columna.

    Retorna:
    df -- DataFrame con la columna completada con ceros a la izquierda.
    """
    # Validaciones
    assert isinstance(df, pd.DataFrame), "El primer parámetro debe ser un DataFrame."
    assert isinstance(columna, str), "El nombre de la columna debe ser una cadena."
    assert columna in df.columns, f"La columna '{columna}' no existe en el DataFrame."
    assert isinstance(n_clave, int), "El número de caracteres debe ser un entero."
    assert n_clave > 0, "El número de caracteres debe ser un entero positivo."

    df[columna] = df[columna].apply(lambda x: str(x).zfill(n_clave))
    return df

def generar_cvegeomun(df: pd.DataFrame, posicion_col: int) -> pd.DataFrame:
    """
    Concatena las claves de entidad y municipio en un DataFrame para formar una nueva columna 'cvegeomun'.
    La nueva columna se ubicará en la posición especificada por `posicion_col`.

    Parámetros:
    ----------
    df : pd.DataFrame
        DataFrame que contiene las columnas 'cve_ent' y 'cve_mun' a concatenar.
    posicion_col : int
        Posición (base 0) en la lista de columnas donde se ubicará la nueva columna 'cvegeomun'.

    Retorna:
    --------
    pd.DataFrame
        DataFrame con la nueva columna 'cvegeomun' añadida en la posición deseada.

    Ejemplo:
    --------
        df = concatenar_claves_mun(df, posicion_col=5)
    """
    # Validaciones
    if not isinstance(df, pd.DataFrame):
        raise ValueError("El parámetro 'df' debe ser un DataFrame.")
    if 'cve_ent' not in df.columns:
        raise ValueError("El DataFrame debe contener una columna 'cve_ent'.")
    if 'cve_mun' not in df.columns:
        raise ValueError("El DataFrame debe contener una columna 'cve_mun'.")
    if not isinstance(posicion_col, int):
        raise ValueError("El parámetro 'posicion_col' debe ser un entero.")
    if not 0 <= posicion_col <= len(df.columns):
        raise IndexError(f"La posición {posicion_col} está fuera del rango de columnas (0-{len(df.columns)}).")

    nueva_columna = df['cve_ent'].str.zfill(2) + df['cve_mun'].str.zfill(3)

    # insertar la nueva columna en la posición deseada
    columnas = list(df.columns)
    columnas.insert(posicion_col, 'cvegeomun')  

    df = df.assign(cvegeomun=nueva_columna)  
    df = df[columnas]  
    return df

def renombrar_columnas(df: pd.DataFrame, dicc: dict) -> pd.DataFrame:
    """
    Renombra las columnas de un DataFrame según un diccionario dado.

    Parámetros:
    df -- DataFrame al que se le renombrarán las columnas.
    dicc -- Diccionario donde las claves son los nombres actuales de las columnas y los valores son los nuevos nombres.

    Retorna:
    df -- DataFrame con las columnas renombradas.

    Ejemplo de uso:
    dicc = {'Enero': 'enero', 'Febrero': 'febrero', 'Marzo': 'marzo', 'Abril': 'abril', 'Mayo': 'mayo'}
    """

    # Validaciones
    assert isinstance(df, pd.DataFrame), "El parámetro df debe ser un DataFrame."
    assert isinstance(dicc, dict), "El parámetro dicc debe ser un diccionario."

    for col in dicc.keys():
        assert col in df.columns, f"La columna '{col}' no existe en el DataFrame."

    df.rename(columns=dicc, inplace=True)
    return df

def reordenar_columnas(df: pd.DataFrame, lista: list) -> pd.DataFrame:
    """
    Reordena las columnas de un DataFrame según el orden especificado en una lista.

    Parámetros:
    df -- DataFrame al que se le reordenarán las columnas.
    lista -- Lista con el orden deseado de las columnas.

    Retorna:
    df -- DataFrame con las columnas reordenadas.

    Ejemplo de uso:
    lista = ['g_id', 'cve_ent', 'nom_ent', 'cve_mun', 'cvegeomun']
    """

    # Validaciones
    assert isinstance(df, pd.DataFrame), "El primer parámetro debe ser un DataFrame."
    assert isinstance(lista, list), "El segundo parámetro debe ser una lista."
    
    for col in lista:
        assert col in df.columns, f"La columna '{col}' no existe en el DataFrame."

    df = df.reindex(columns=lista)
    return df

def mover_columnas(df: pd.DataFrame, al_inicio: list = None, al_final: list = None) -> pd.DataFrame:
    """
    Reordena columnas moviendo un subconjunto específico al inicio o al final.

    Parámetros:
    ----------
    df : pd.DataFrame
        DataFrame original.
    al_inicio : list, opcional
        Lista de columnas que deben moverse al inicio.
    al_final : list, opcional
        Lista de columnas que deben moverse al final.

    Retorna:
    --------
    pd.DataFrame
        DataFrame con las columnas reordenadas.
    """
    al_inicio = al_inicio or []
    al_final = al_final or []

    # Validar que las columnas especificadas estén en el DataFrame
    al_inicio = [col for col in al_inicio if col in df.columns]
    al_final = [col for col in al_final if col in df.columns]

    # Determinar el resto de las columnas
    resto = [col for col in df.columns if col not in al_inicio + al_final]

    # Reordenar las columnas
    nuevo_orden = al_inicio + resto + al_final
    return df[nuevo_orden]


def convertir_columna_texto(df: pd.DataFrame, columna: str) -> pd.DataFrame:
    """
    Convierte el tipo de dato de una columna a texto (cadena).

    Parámetros:
    df -- DataFrame al que se le cambiará el tipo de dato de una columna.
    columna -- Nombre de la columna a cambiar.

    Retorna:
    df -- DataFrame con la columna convertida a texto.
    """

    # Validaciones
    assert isinstance(df, pd.DataFrame), "El primer parámetro debe ser un DataFrame."
    assert isinstance(columna, str), "El nombre de la columna debe ser una cadena."
    assert columna in df.columns, f"La columna '{columna}' no existe en el DataFrame."

    df[columna] = df[columna].astype(str)
    return df

def convertir_columna_entero(df: pd.DataFrame, columna: str) -> pd.DataFrame:
    """
    Convierte el tipo de dato de una columna a entero.

    Parámetros:
    df -- DataFrame al que se le cambiará el tipo de dato de una columna.
    columna -- Nombre de la columna a cambiar.

    Retorna:
    df -- DataFrame con la columna convertida a entero.
    """

    # Validaciones
    assert isinstance(df, pd.DataFrame), "El primer parámetro debe ser un DataFrame."
    assert isinstance(columna, str), "El nombre de la columna debe ser una cadena."
    assert columna in df.columns, f"La columna '{columna}' no existe en el DataFrame."
    
    try:
        df[columna] = df[columna].astype(int)
    except ValueError:
        raise ValueError(f"No se pudo convertir la columna '{columna}' a entero. Verifica que todos los valores sean numéricos y no nulos.")
    return df

def convertir_columna_real(df: pd.DataFrame, columna: str) -> pd.DataFrame:
    """
    Convierte el tipo de dato de una columna a real (float).

    Parámetros:
    df -- DataFrame al que se le cambiará el tipo de dato de una columna.
    columna -- Nombre de la columna a cambiar.

    Retorna:
    df -- DataFrame con la columna convertida a real (float).
    """

    # Validaciones
    assert isinstance(df, pd.DataFrame), "El primer parámetro debe ser un DataFrame."
    assert isinstance(columna, str), "El nombre de la columna debe ser una cadena."
    assert columna in df.columns, f"La columna '{columna}' no existe en el DataFrame."
    
    try:
        df[columna] = df[columna].astype(float)
    except ValueError:
        raise ValueError(f"No se pudo convertir la columna '{columna}' a tipo real (float). Verifica que todos los valores sean numéricos y no nulos.")
    return df

def identificar_nulos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Identifica los valores nulos de un DataFrame y los presenta en formato tabular.

    Parámetros:
    ----------
    df : pd.DataFrame
        DataFrame al que se le identificarán los valores nulos.

    Retorna:
    --------
    pd.DataFrame
        DataFrame con los registros que tienen al menos un valor nulo.
        Si no hay nulos, retorna None.
    """
    # Validaciones
    assert isinstance(df, pd.DataFrame), "El parámetro debe ser un DataFrame."

    total_nulos = df.isnull().sum().sum()

    if total_nulos == 0:
        print("No hay nulos en el DataFrame.")
        return None
    else:
        print(f"Total de nulos en el DataFrame: {total_nulos}\n")
        
        # Crear un df resumen de los nulos por columna
        nulos_por_columna = df.isnull().sum()
        nulos_resumen = pd.DataFrame({
            "Columna": nulos_por_columna.index,
            "Nulos": nulos_por_columna.values,
            "Porcentaje": (nulos_por_columna / len(df) * 100).round(2)
        })
        
        nulos_resumen = nulos_resumen[nulos_resumen["Nulos"] > 0]
        
        print("Resumen de nulos por columna:\n")
        print(tabulate(nulos_resumen, headers="keys", tablefmt="pretty", showindex=False))
        
        df_nulos = df[df.isnull().any(axis=1)]
        
        columnas_con_nulos = df.columns[df.isnull().any()].tolist()
        print("\nColumnas con valores nulos:", ", ".join(columnas_con_nulos))
        
        return df_nulos
    
def cambiar_tipo_columna(df: pd.DataFrame, lista: list, tipo: str) -> pd.DataFrame:
    """
    Cambia el tipo de dato de varias columnas en un DataFrame.

    Parámetros:
    df -- DataFrame al que se le cambiará el tipo de dato de una o más columnas.
    lista -- Lista con los nombres de las columnas a cambiar.
    tipo -- Tipo de dato al que se cambiarán las columnas ("texto", "entero", "real").

    Retorna:
    df -- DataFrame con las columnas convertidas al tipo especificado.
    """

    # Validaciones
    assert isinstance(df, pd.DataFrame), "El primer parámetro debe ser un DataFrame."
    assert isinstance(lista, list), "El segundo parámetro debe ser una lista."
    assert tipo in ["texto", "entero", "real"], "El tipo debe ser 'texto', 'entero' o 'real'."

    # Conversión de tipo según el tipo especificado
    for col in lista:
        assert col in df.columns, f"La columna '{col}' no existe en el DataFrame."
        
        if tipo == "texto":
            df[col] = df[col].astype(str)
        elif tipo == "entero":
            try:
                df[col] = df[col].astype(int)
            except ValueError:
                raise ValueError(f"No se pudo convertir la columna '{col}' a entero. Verifica que todos los valores sean numéricos y no nulos.")
        elif tipo == "real":
            try:
                df[col] = df[col].astype(float)
            except ValueError:
                raise ValueError(f"No se pudo convertir la columna '{col}' a real. Verifica que todos los valores sean numéricos y no nulos.")
    
    return df

def cambiar_valor_df(df: pd.DataFrame, valor_inicial, valor_final) -> pd.DataFrame:
    """
    Cambia un valor específico por otro en todas las columnas de un DataFrame.

    Parámetros:
    df -- DataFrame al que se le cambiará el valor.
    valor_inicial -- Valor a cambiar.
    valor_final -- Valor por el que se cambiará.

    Retorna:
    df -- DataFrame con el valor cambiado.
    """

    # Validaciones
    assert isinstance(df, pd.DataFrame), "El primer parámetro debe ser un DataFrame."

    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].replace(valor_inicial, valor_final)

    return df

def cambiar_valor_columna(df: pd.DataFrame, columna: str, valor_inicial, valor_final) -> pd.DataFrame:
    """
    Cambia un valor específico por otro en una columna de un DataFrame.

    Parámetros:
    df -- DataFrame al que se le cambiará el valor.
    columna -- Nombre de la columna en la que se realizará el cambio.
    valor_inicial -- Valor a cambiar.
    valor_final -- Valor por el que se cambiará.

    Retorna:
    df -- DataFrame con el valor cambiado en la columna especificada.
    """

    # Validaciones
    assert isinstance(df, pd.DataFrame), "El primer parámetro debe ser un DataFrame."
    assert isinstance(columna, str), "El nombre de la columna debe ser una cadena."
    assert columna in df.columns, f"La columna '{columna}' no existe en el DataFrame."

    df[columna] = df[columna].replace(valor_inicial, valor_final)
    return df

def identificar_valores_unicos_df(df: pd.DataFrame):
    """
    Identifica y muestra el número de valores únicos en cada columna de un DataFrame.

    Parámetros:
    df -- DataFrame del cual se identificarán los valores únicos en cada columna.
    """

    # Validaciones
    assert isinstance(df, pd.DataFrame), "El parámetro debe ser un DataFrame."

    for columna in df.columns:
        valores_unicos = df[columna].nunique()
        print(f"Número de valores únicos para la columna '{columna}': {valores_unicos}")

def identificar_valores_unicos_columna(df: pd.DataFrame, nombre_col: str):
    """
    Identifica los valores únicos de una columna específica en un DataFrame.

    Parámetros:
    df -- DataFrame del cual se identificarán los valores únicos en la columna especificada.
    nombre_col -- Nombre de la columna a identificar los valores únicos.

    Retorna:
    valores_unicos -- Lista con los valores únicos de la columna.
    """

    # Validaciones
    assert isinstance(df, pd.DataFrame), "El primer parámetro debe ser un DataFrame."
    assert isinstance(nombre_col, str), "El nombre de la columna debe ser una cadena."
    assert nombre_col in df.columns, f"La columna '{nombre_col}' no existe en el DataFrame."

    valores_unicos = df[nombre_col].unique().tolist()
    return valores_unicos

def campos_df(df: pd.DataFrame):
    '''
    Función que retorna los campos de un dataframe de pandas, los campos se 
    retornan en una lista.
    '''

    assert isinstance(df, pd.DataFrame), "El parámetro debe ser un DataFrame."

    columnas = list(df.columns)
    print(columnas)
    return(columnas)