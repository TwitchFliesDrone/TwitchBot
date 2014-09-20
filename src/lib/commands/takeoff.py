# coding: utf8

import requests, json

def takeoff():
	
	port = 3050
	
#	try:
	r = requests.get('http://localhost:' + str(port) + '/control/takeoff')
#	except:
#		return 'Error!'

	return 'Taken off!'
