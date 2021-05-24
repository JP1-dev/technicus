### crawls earthquake + wildfire data and writes it to .msgpack files ###

import requests
import schedule
import msgpack
import pandas as pd
from io import StringIO


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
    response= requests.get('https://firms.modaps.eosdis.nasa.gov/data/active_fire/modis-c6.1/csv/MODIS_C6_1_Global_24h.csv')
    print('data retrieved')
    wildfire_df= pd.read_csv(StringIO(response.content.decode()), sep=',')
    wildfire_data= []

    for i in range(wildfire_df.shape[0]):
        wildfire_data.append([
            float(wildfire_df.iloc[i]['latitude']),
            float(wildfire_df.iloc[i]['longitude']),
            int(wildfire_df.iloc[i]['confidence'])
        ])

    print('writing')
    with open('wildfire_data.msgpack', 'wb') as file:
        file.write(msgpack.packb({'data': wildfire_data}))
    print('wildfires done')
    return wildfire_data


def master():
    get_earthquake_data()
    get_wildfire_data()


if __name__ == '__main__':
    schedule.every(5000).seconds.do(master)
    while True:
        schedule.run_pending()
