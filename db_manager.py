#fetches data from database, analyze() is writing to database
import psycopg2
import crawler
import analyzer
import time
import msgpack


def connect():
    connection= psycopg2.connect(
        user= 'jojo',
        password= 'postgresqlisgreat',
        host= 'localhost',
        port= '5432',
        database= 'technicus'
    )
    return connection


def eq(min_mag):
    conn= connect()
    cursor= conn.cursor()
    cursor.execute(f"SELECT longitude, latitude, mag,breakLength, time, type, tsunami, alert, place FROM earthquakes WHERE mag >= {min_mag};")
    data= cursor.fetchall()
    cursor.close()
    conn.close()
    return data




#connection= connect()
#cursor= connection.cursor()
#cursor.execute(f"SELECT longitude, latitude, mag, place, time, type, tsunami, alert FROM earthquakes WHERE mag >= 2.8;")


def read_file(name):
    if name == 'eq':
        with open('earthquake_data.msgpack', 'rb') as file:
            data= msgpack.unpackb(file.read())
            return data

    elif name == 'wildfires':
        with open('wildfire_data.msgpack', 'rb') as file:
            data= msgpack.unpackb(file.read())
            return data


def analyze():
    #worker= crawler.Worker_earthquakes('id1')
    #worker.run()
    #print('ok')
    #time.sleep(5)
    analyzer.process_earthquakes(read_file('eq'))
    analyzer.process_wildfires(read_file('wildfires'))
    print('done')
