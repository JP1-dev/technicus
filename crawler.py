### crawls earthquake + wildfire data and writes it to .msgpack files ###

import requests
import json
#import psycopg2
#import time
#import threading
from datetime import datetime
#from analyzer import *
import schedule
import msgpack

def get_earthquake_data():
    print('running...')
    response= requests.get('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson')
    print('request done')
    earthquake_data= response.json()
    print('writing file...')
    with open('earthquake_data.msgpack', 'wb') as file:
        file.write(msgpack.packb(earthquake_data))
    print('earthquakes done')


def get_wildfire_data():
    print('running...')
    response= requests.get('https://services3.arcgis.com/T4QMspbfLg3qTGWY/arcgis/rest/services/Public_Wildfire_Perimeters_View/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')
    print('data retrieved')
    wildfire_data= response.json()
    print('writing')
    with open('wildfire_data.msgpack', 'wb') as file:
        file.write(msgpack.packb(wildfire_data))
    print('wildfires done')

def master():
    get_earthquake_data()
    get_wildfire_data()



if __name__ == '__main__':
    schedule.every(10).seconds.do(master)
    while True:
        schedule.run_pending()




"""
#database related stuff
def connect():
        connection= psycopg2.connect(
                user= 'jojo',
                password= 'postgresqlisgreat',
                host= 'localhost',
                port= '5432',
                database= 'technicus'
        )
        return connection



class Worker_earthquakes(threading.Thread):
        def __init__(self, threadID):
                threading.Thread.__init__(self)
                self.iD= threadID
                self.rqu= requests
                self.earthquake_data= {}

        def run(self):
                i= 0
                while i<1:
                        response= self.rqu.get('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_day.geojson')
                        self.earthquake_data= response.json()
                        #time.sleep(1800)
                        i+= 1


class Worker_wildfires(threading.Thread):
    def __init__(self, threadID):
        threading.Thread.__init__(self)
        self.iD= threadID
        self.rqu= requests
        self.wildfire_data= {}

    def run(self):
        i= 0
        while i<1:
            response= self.rqu.get('https://services3.arcgis.com/T4QMspbfLg3qTGWY/arcgis/rest/services/Public_Wildfire_Perimeters_View/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')
            self.wildfire_data= response.json()
            #time.sleep(21600)
            i+= 1


class Supervisor():
    def __init__(self):
        self.earthquakes= Worker_earthquakes(1)
        self.wildfires= Worker_wildfires(2)

    def go(self):
        self.earthquakes.start()
        self.wildfires.start()

        time.sleep(15)
        process_earthquakes(self.earthquakes.earthquake_data)
"""
        
#import schedule
# schedule.every(1).seconds.do(function)
#while True: sched#while True: schedule.run_pending()      
#ule.run_pending()      