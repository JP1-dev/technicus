from flask import Flask, request, jsonify, redirect, url_for
from datetime import datetime
import authentication
from request_processing import analyse_request, process


app= Flask(__name__)

authenticater= authentication.Authentication()

key= '6ru6dsh5kD8oHC79a_78segQ5_eR96' #this is obviously not in production


@app.route('/')
def index():
    index_dic= {
      "status": "FUCK OFF",
      "time": datetime.now()
    }
    return jsonify(index_dic)



@app.route('/api')
def api():
    isAccepted= authenticater.check_client(request.remote_addr)

    if isAccepted:
        isSecure= analyse_request(request.headers)

        if isSecure:
            response= process(request.headers)
            return response

        else:
            return '{"status": "requests contains unallowed header"}'
       
    else:
        return '{"data": "key required"}'
    



@app.route('/api/login')
def login():
    try:
        key_from_request= request.headers.get('key')
        if key_from_request == key:
            authenticater.add_client(request.remote_addr)
            print(f"{request.remote_addr} added") 
            return '{"status": "key accepted"}'
        else:
            return '{"error": "key not accepted"}'
    
    except BaseException:
        return '{"error": "an error occured"}'
        



if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')
