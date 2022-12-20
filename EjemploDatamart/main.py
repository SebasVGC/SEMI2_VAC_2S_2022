#Las librerias necesarias
import pyodbc
import pandas as pd

from imprimir import *
from creacion import * #crear tablas datawarehouse
from creacion1 import * #crear tablas datamart1
from creacion2 import * #crear tablas datamart2
from consultas import *
import config
import config1
import config2

import logging

#Configurar nuestro log

logger = logging.getLogger('Semi_2_Ejemplo')
logger.setLevel(logging.DEBUG)
ch = logging.FileHandler('logs.log', 'w',encoding = 'UTF-8')
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

#Configurar nuestra conexion

CONNECTION_STRING = f"DRIVER={{{config.driver}}};SERVER={config.server};UID={config.sql_user};PWD={config.sql_password};DATABASE={config.database}"
CONNECTION_STRING1 = f"DRIVER={{{config1.driver}}};SERVER={config1.server};UID={config1.sql_user};PWD={config1.sql_password};DATABASE={config1.database}"
CONNECTION_STRING2 = f"DRIVER={{{config2.driver}}};SERVER={config2.server};UID={config2.sql_user};PWD={config2.sql_password};DATABASE={config2.database}"

logger.info("Iniciando nuestra aplicacion")

logger.info(" CONNECTION_STRING: ".center(80, "-"))
before, after = CONNECTION_STRING.split("PWD=")
before, after = CONNECTION_STRING1.split("PWD=")
before, after = CONNECTION_STRING2.split("PWD=")
logger.info(before + f"PWD=<{len(after)} characters>")

logger.info("Iniciando la realizacion de la conexion")
conn = pyodbc.connect(CONNECTION_STRING,autocommit=True)
logger.info("Conexion realizada con exito")

logger.info("Iniciando la realizacion de la conexion con datamart1")
conn1 = pyodbc.connect(CONNECTION_STRING1,autocommit=True)
logger.info("Conexion realizada con exito")

logger.info("Iniciando la realizacion de la conexion con datamart2")
conn2 = pyodbc.connect(CONNECTION_STRING2,autocommit=True)
logger.info("Conexion realizada con exito")

def main():
    archivo=open('resultados.txt','w',encoding="utf-8")
    archivo.close()
    menu()

def menu():
    while True:
        print_main_menu()
        opcion = input('Seleccione una opcion: ')
        if opcion=='1':
            logger.info("Usuario selecciona opcion de creacion de modelo")
            creacion()
        elif opcion=='2':
            logger.info('Usuario selecciona opcion de ejecutar consultas')
            creacion2()
        elif opcion=='3':
            logger.info('Usuario selecciona opcion de ejecutar consultas')
            consultas(CONSULTA1,"SELECT * FROM")
        elif opcion=='4':
            logger.info('Usuario selecciona opcion de crear datamarts')
            creacionDatamarts()

        else:
            conn.close() #Me desconecto del datawarehouse
            conn1.close() #Me desconecto del datamart 1
            conn2.close() #Me desconecto del datamart 2
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
        data = pd.read_csv("songs_normalize.csv", encoding='utf-8')
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
        i = i +1
        # if(i==0):
        #     i = i +1
        #     continue
        artist = str(row[1].replace("'","''"))
        song = str(row[2].replace("'","''"))
        genre = str(row[18].replace("'","''"))
        query = (f'INSERT INTO temporal VALUES(\'{artist}\',\'{song}\',{row[3]},\'{row[4]}\',{row[5]},{row[6]},{row[7]},{row[8]},{row[9]},{row[10]},{row[11]},{row[12]},{row[13]},{row[14]},{row[15]},{row[16]},{row[17]},\'{genre}\')')
        logger.info(query)
        #print(query)

        cursor.execute(query)
    #logger(cursor.execute("SELECT * FROM temporal LIMIT 1"))
    logger.info(f'Se insertaron correctamente {i} filas')

def creacion2():
    logger.info("Procediendo a crear modelo...")
    cursor = conn.cursor()
    logger.info("Creando las tablas necesarias")
    cursor.execute(ARTIST_CREATION)
    cursor.execute(GENRE_CREATION)
    cursor.execute(SONG_CREATION)
    cursor.execute(PLAYS_CREATION)
    cursor.execute(FK_CREATION1)
    cursor.execute(FK_CREATION2)
    cursor.execute(FK_CREATION3)
    logger.info("Comenzando a procesar el dataset")
    cargar_artistas()
    cargar_generos()
    cargar_canciones()
    cargar_plays()

def cargar_artistas():
    cursor = conn.cursor()
    query = (f'INSERT INTO artist SELECT DISTINCT artist FROM temporal')
    logger.info(query)
    try:
        cursor.execute(query)
        logger.info(f'Se insertaron correctamente los artistas')
    except Exception as e:
        logger.error(e)
        conn.close()
        exit()

def cargar_generos():
    cursor = conn.cursor()
    query = (f'INSERT INTO genre SELECT DISTINCT genre FROM temporal')
    logger.info(query)
    try:
        cursor.execute(query)
        logger.info(f'Se insertaron correctamente los generos')
    except Exception as e:
        logger.error(e)
        conn.close()
        exit()

def cargar_canciones():
    cursor = conn.cursor()
    query = (f'INSERT INTO song SELECT DISTINCT t.song,t.duration_ms,t.explicit,t.year,t.popularity,t.danceability,t.energy,t.llave,t.loudness,t.mode,t.speechiness,t.acousticness,t.instrumentalness,t.liveness,t.valence,t.tempo,a.id,g.id FROM temporal t, artist a, genre g WHERE t.artist=a.name_ AND t.genre=g.name_ ;')
    logger.info(query)
    try:
        cursor.execute(query)
        logger.info(f'Se insertaron correctamente las canciones')
    except Exception as e:
        logger.error(e)
        conn.close()
        exit()

def cargar_plays():
    cursor = conn.cursor()
    query = (f'SELECT * FROM temporal')
    try:
        cursor.execute(query)
        resultado=cursor.fetchall()
        for row_ in resultado:
            # print(item.song)
            song = str(row_.song.replace("'","''"))
            query = (f'INSERT INTO plays SELECT s.id FROM song s WHERE ( s.name_=\'{song}\' AND s.year={row_.year} AND s.popularity={row_.popularity} AND s.tempo={row_.tempo} )')
            logger.info(query)
            cursor.execute(query)

        logger.info(f'Se insertaron correctamente las reproducciones')
    except Exception as e:
        logger.error(e)
        conn.close()
        exit()


def consultas(consulta_,titulo_):
    try:
        cursor = conn.cursor()
        query = consulta_
        logger.info(query)
        cursor.execute(query)
        data = cursor.fetchall()
        # print(data)
        archivo=open('resultados.txt','a',encoding="utf-8")
        cadena=""
        cadena+=titulo_+"\n"
        for row_ in data:
            cadena+="\t"
            for element_ in row_:
                cadena+=str(element_)+"\t"
            cadena+="\n"
        cadena+="\n"
        archivo.write(cadena)
        archivo.close()

    except Exception as e:
        logger.error(e)
        conn.close()
        exit()


def creacionDatamarts():
    #crear datamart 1
    logger.info("Procediendo a crear...")
    logger.info("Eliminando tablas...")
    cursor1 = conn1.cursor()
    cursor1.execute(DROP_TABLES1)
    logger.info("Tablas eliminadas correctamente del datamart1")
    logger.info("Creando las tablas necesarias del datamart1")
    logger.info("Creando tabla temporal del datamart1")
    cursor1.execute(TEMPORAL_CREATION1)
    logger.info("Creando las tablas del datamart1")
    cursor1.execute(ARTIST_CREATION1)
    logger.info("Comenzando a procesar el dataset del datamart1")
    #crear datamart 2
    cursor2 = conn2.cursor()
    cursor2.execute(DROP_TABLES2)
    logger.info("Tablas eliminadas correctamente del datamart2")
    logger.info("Creando las tablas necesarias del datamart2")
    logger.info("Creando tabla temporal del datamart2")
    cursor2.execute(TEMPORAL_CREATION2)
    logger.info("Creando las tablas del datamart2")
    cursor2.execute(GENRE_CREATION2)
    logger.info("Comenzando a procesar el dataset del datamart2")
    llenarDatamart1()
    llenarDatamart2()

def llenarDatamart1():
    try:
        cursor = conn.cursor() #nos conectamos al DW central para obtener datos
        query = 'SELECT DISTINCT name_ FROM artist'
        logger.info(query)
        cursor.execute(query)
        data = cursor.fetchall()
        print(data[1].name_)

        for row_ in data:
            cursor1 = conn1.cursor() #nos conectamos al datamart 1
            artista = str(row_.name_.replace("'","''"))
            queryDatamart1 = (f'INSERT INTO artist (name_) VALUES(\'{artista}\')')
            print(queryDatamart1)
            logger.info(queryDatamart1)
            cursor1.execute(queryDatamart1)

    except Exception as e:
        logger.error(e)
        conn.close()
        exit()
    
def llenarDatamart2():
    try:
        cursor = conn.cursor() #nos conectamos al DW central para obtener datos
        query = 'SELECT DISTINCT name_ FROM genre'
        logger.info(query)
        cursor.execute(query)
        data = cursor.fetchall()
        print(data[1].name_)

        for row_ in data:
            cursor2 = conn2.cursor() #nos conectamos al datamart 1
            genero = str(row_.name_.replace("'","''"))
            queryDatamart2 = (f'INSERT INTO genre (name_) VALUES(\'{genero}\')')
            print(queryDatamart2)
            logger.info(queryDatamart2)
            cursor2.execute(queryDatamart2)

    except Exception as e:
        logger.error(e)
        conn.close()
        exit()


if __name__ == "__main__":
    main()
    logger.info('Aplicacion finalizada')
