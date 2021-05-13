#contains functions to extract the needed data from a dictionary and puts it into a database
import psycopg2
import time
import math

#connect
def connect():
    connection= psycopg2.connect(
        user= 'jojo',
        password= 'postgresqlisgreat',
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
        breakLength= round(getBreakLength(mag), 5)
        #base= 0.0001
        #area_underground= base*(10**mag)
        #radius_underground= math.sqrt(area_underground/math.pi)
        #count= 0
        #radius origin in m, because of flutter
        #try:
        #    radius_origin= math.sqrt(radius_underground**2 - depth**2)*1000 

        #except BaseException:
        #    count+= 1
        #    radius_origin= 1
        
        place= element["properties"]["place"]
        timeConverted= time.localtime(int(element["properties"]["time"])/1000)
        typeS= element["properties"]["type"] 
        tsunami= bool(element["properties"]["tsunami"])
        alert= element["properties"]["alert"]
        

        timeS= f"{timeConverted[0]}-{timeConverted[1]}-{timeConverted[2]}-{timeConverted[3]}-{timeConverted[4]}-{timeConverted[5]}"

     
        cursor.execute(f"""{baseString} VALUES('{id}',{longitude},{latitude},{mag},{breakLength},{depth},'{place}','{timeS}','{typeS}', {str(tsunami).lower()}, '{alert}')""")

    conn.commit()   



def getBreakLength(mag):
    return 2 * 5 ** (mag-5)
    

"""
$$$$$$$$$$$$$$$$$$$$$$$$$$
"""


def process_wildfires(wildfires):
    conn= connect()
    cursor= conn.cursor()
    baseString= """INSERT INTO wildfires(id, incidentName, shapeArea, isVisible, polygonCoordinates)"""

    for element in wildfires['features']:
        id= element['attributes']['GlobalID']
        incidentName= element['attributes']['IncidentName']
        shapeArea= element['attributes']['Shape__Area']
        isVisible= str(element['attributes']['IsVisible'])
        polygonCoordinates= str(element['geometry']['rings'][0])

        cursor.execute(f"""{baseString} VALUES('{id}', '{incidentName}', {float(shapeArea)}, '{isVisible}', '{polygonCoordinates}')""")

    conn.commit()




#M = log (I/In)Stranger: Where I is intensity and In is arbitrary intensity


