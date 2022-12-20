DROP_TABLES1=('DROP TABLE if exists temporal;DROP TABLE if exists artist;')

TEMPORAL_CREATION1=('CREATE TABLE temporal(artist VARCHAR(50),song VARCHAR(500),duration_ms int,explicit bit,'
    'year int,popularity decimal(10,4),danceability decimal(10,4),energy decimal(10,4),llave int,' 
    'loudness decimal(10,4),mode decimal(10,4),speechiness decimal(10,4),acousticness decimal(10,4),'
    'instrumentalness decimal(10,7),liveness decimal(10,4),valence decimal(10,4),tempo decimal(10,4),'
    'genre varchar(50) )')

ARTIST_CREATION1=('CREATE TABLE artist ('
    'id INTEGER IDENTITY(1,1) PRIMARY KEY,'
    'name_ VARCHAR(50)'
    ');')
