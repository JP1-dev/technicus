import requests
import json
import msgpack


def main():
    response= requests.get('https://services3.arcgis.com/T4QMspbfLg3qTGWY/arcgis/rest/services/Public_Wildfire_Perimeters_View/FeatureServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json')
    with open('wildfires.txt', 'w') as file:
	    file.write(str(json.dumps(response.json())))

if __name__ == '__main__':
    main()



















