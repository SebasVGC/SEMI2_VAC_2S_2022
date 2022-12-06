#Las librerias necesarias
import pyodbc
import pandas as pd

from imprimir import *
from creacion import *
from consultas import *
import config
import logging

#Configurar nuestro log

logger = logging.getLogger('Semi_2_Ejemplo')
logger.setLevel(logging.DEBUG)
ch = logging.FileHandler('logs.log')
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

#Configurar nuestra conexion

CONNECTION_STRING = f"DRIVER={{{config.driver}}};SERVER={config.server};UID={config.sql_user};PWD={config.sql_password};DATABASE={config.database}"

logger.info("Iniciando nuestra aplicacion")

logger.info(" CONNECTION_STRING: ".center(80, "-"))
before, after = CONNECTION_STRING.split("PWD=")
logger.info(before + f"PWD=<{len(after)} characters>")

logger.info("Iniciando la realizacion de la conexion")
conn = pyodbc.connect(CONNECTION_STRING,autocommit=True)
logger.info("Conexion realizada con exito")

def main():
    menu()

def menu():
    while True:
        print_main_menu()
        opcion = input('Seleccione una opcion: ')
        if opcion=='1':
            logger.info("Usuario selecciona opcion de creacion")
            creacion()
        elif opcion=='2':
            logger.info('Usuario selecciona opcion de ejecutar consultas')
            consultas(CONSULTA1)
        else:
            conn.close()
            logger.info('Conexion finalizada')
            exit()
            
def creacion():
    logger.info("Procediendo a crear...")
    logger.info("Eliminando tablas...")
    cursor = conn.cursor()
    cursor.execute(DROP_TABLES)
    logger.info("Tablas eliminadas correctamente")
    logger.info("Creando las tablas necesarias")
    logger.info("Creando tabla temporal")
    cursor.execute(TEMPORAL_CREATION)
    logger.info("Comenzando a procesar el dataset")
    try:
        data = pd.read_csv("songs_normalize.csv")
        df = pd.DataFrame(data)
        logger.info("Dataset leido exitosamente")
        cargar_temporal(df)
    except Exception as e:
        logger.error(e)
        conn.close()
        exit()

def cargar_temporal(df):
    cursor = conn.cursor()
    i = 0
    for row in df.itertuples():
        if(i==0):
            i = i +1
            continue
        artist = str(row[1].replace("'","''"))
        song = str(row[2].replace("'","''"))
        genre = str(row[18].replace("'","''"))
        query = (f'INSERT INTO temporal VALUES(\'{artist}\',\'{song}\',{row[3]},\'{row[4]}\',{row[5]},{row[6]},{row[7]},{row[8]},{row[9]},{row[10]},{row[11]},{row[12]},{row[13]},{row[14]},{row[15]},{row[16]},{row[17]},\'{genre}\')')
        logger.info(query)
        #print(query)

        cursor.execute(query)
    #logger(cursor.execute("SELECT * FROM temporal LIMIT 1"))
    logger.info(f'Se insertaron correctamente {i} filas')

def consultas(consulta_):
    try:
        cursor = conn.cursor()
        query = consulta_
        logger.info(query)
        cursor.execute(query)
        data = cursor.fetchall()
        print(data)
        
    except Exception as e:
        logger.error(e)
        conn.close()
        exit()

if __name__ == "__main__":
    main()
    logger.info('Aplicacion finalizada')