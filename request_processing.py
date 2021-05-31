import json
import db_manager


#list which contains the allowed header keys
ALLOWED_HEADERS= ["Host", "Connection", "Cache-Control", "Upgrade-Insecure-Requests", "User-Agent",
"Accept-Encoding", "Accept-Language","Content-Length","Accept","User-agent","Key","Earthquakes", "Wildfires","MinMag"]


def analyse_request(request_headers):
	isSecure= True
	for key in request_headers.keys():
		if key in ALLOWED_HEADERS:
			continue
		else:
			print(key)
			isSecure= True #FALSEEEEE

	return isSecure


def process(request_headers):
	if 'Earthquakes' in request_headers.keys():
		try:
			min_mag= float(request_headers["Earthquakes"])
		except BaseException:
			return '{"status": "error"}'
		data= db_manager.get_earthquakes(min_mag)
		return data

	elif 'Wildfires' in request_headers.keys():
		return str(db_manager.get_wildfires())


