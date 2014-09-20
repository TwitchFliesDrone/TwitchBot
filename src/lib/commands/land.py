# coding: utf8

import requests, json

def land():
	
	port = 3050
	
#	try:
	r = requests.get('http://localhost:' + str(port) + '/control/land')
#	except:
#		return 'Error!'

	return 'Landed!'
