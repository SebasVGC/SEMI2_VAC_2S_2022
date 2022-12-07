DROP_TABLES=('DROP TABLE if exists temporal;DROP TABLE if exists plays;DROP TABLE if exists song;DROP TABLE if exists artist;DROP TABLE if exists genre;')

TEMPORAL_CREATION=('CREATE TABLE temporal(artist VARCHAR(50),song VARCHAR(500),duration_ms int,explicit bit,'
    'year int,popularity decimal(10,4),danceability decimal(10,4),energy decimal(10,4),llave int,' 
    'loudness decimal(10,4),mode decimal(10,4),speechiness decimal(10,4),acousticness decimal(10,4),'
    'instrumentalness decimal(10,7),liveness decimal(10,4),valence decimal(10,4),tempo decimal(10,4),'
    'genre varchar(50) )')

ARTIST_CREATION=('CREATE TABLE artist ('
    'id INTEGER IDENTITY(1,1) PRIMARY KEY,'
    'name_ VARCHAR(50)'
    ');')


GENRE_CREATION=('CREATE TABLE genre ('
    'id INTEGER IDENTITY(1,1) PRIMARY KEY,'
    'name_ VARCHAR(50)'
    ');')

SONG_CREATION=('CREATE TABLE song ('
    'id INTEGER IDENTITY(1,1) PRIMARY KEY,'
    'name_ VARCHAR(500),'
    'duration_ms int,explicit bit,'
    'year int,popularity decimal(10,4),danceability decimal(10,4),energy decimal(10,4),llave int,' 
    'loudness decimal(10,4),mode decimal(10,4),speechiness decimal(10,4),acousticness decimal(10,4),'
    'instrumentalness decimal(10,7),liveness decimal(10,4),valence decimal(10,4),tempo decimal(10,4),'
    'artist_id INTEGER,'
    'genre_id INTEGER,'
    ');')

PLAYS_CREATION=('CREATE TABLE plays ('
    'id INTEGER IDENTITY(1,1) PRIMARY KEY,'
    'song_id INTEGER'
    ');')

FK_CREATION1=('ALTER TABLE song '
    'ADD CONSTRAINT song_artist_fk FOREIGN KEY ( artist_id )'
    'REFERENCES artist ( id )'
    'ON DELETE CASCADE;'
    ';')

FK_CREATION2=('ALTER TABLE song '
    'ADD CONSTRAINT song_genre_fk FOREIGN KEY ( genre_id )'
    'REFERENCES genre ( id )'
    'ON DELETE CASCADE;'
    ';')

FK_CREATION3=('ALTER TABLE plays '
    'ADD CONSTRAINT plays_song_fk FOREIGN KEY ( song_id )'
    'REFERENCES song ( id )'
    'ON DELETE CASCADE;'
    ';')