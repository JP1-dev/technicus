import msgpack
import json


dic= {
    'meta':{
        'name': 'name',
        'id': '45D8ilaQ',
        'list': [8,9,42]
    },
    'number': 42
}

#with open('data.msgpack', 'wb') as file:
#    file.write(msgpack.packb(dic))

with open('data.msgpack', 'rb') as file:
    data= msgpack.unpackb(file.read())
    print(data)
    