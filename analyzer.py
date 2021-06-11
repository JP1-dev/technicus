#contains functions to extract the needed data from a dictionary and puts it into a database
import psycopg2
import time

#connect
def connect():
    connection= psycopg2.connect(
        user= 'jojo',
        password= 'postgresql4evver', #mega password
        host= 'localhost',
        port= '5432',
        database= 'technicus'
    )
    return connection


def process_earthquakes(earthquakes):
    conn= connect()
    cursor= conn.cursor()
    baseString= 'INSERT INTO earthquakes(id,longitude, latitude,mag,breakLength,depth, place,time,type,tsunami,alert)'
    
    for element in earthquakes["features"]:
        id= element["id"].replace(',', '')
        longitude= float(element["geometry"]["coordinates"][0])
        latitude= float(element["geometry"]["coordinates"][1])
        mag= float(element["properties"]["mag"])
        depth= round(float(element["geometry"]["coordinates"][2]), 3)
        breakLength= round(2 * 5 ** (mag-5), 5)
        place= element["properties"]["place"]
        timeConverted= time.localtime(int(element["properties"]["time"])/1000)
        typeS= element["properties"]["type"] 
        tsunami= bool(element["properties"]["tsunami"])
        alert= element["properties"]["alert"]
        timeS= f"{timeConverted[0]}-{timeConverted[1]}-{timeConverted[2]}-{timeConverted[3]}-{timeConverted[4]}-{timeConverted[5]}"

        cursor.execute(f"""{baseString} VALUES('{id}',{longitude},{latitude},{mag},{breakLength},{depth},'{place}','{timeS}','{typeS}', {str(tsunami).lower()}, '{alert}')""")

    conn.commit()   


def process_wildfires(wildfires):
    conn= connect()
    cursor= conn.cursor()
    baseString= """INSERT INTO wildfires(latitude, longitude, confidence)"""
    for fire in wildfires['data']:
        latitude= fire[0]
        longitude= fire[1]
        confidence= fire[2]

        cursor.execute(f"""{baseString} VALUES({latitude}, {longitude},{confidence})""")

    conn.commit()



#M = log (I/In)Stranger: Where I is intensity and In is arbitrary intensity
