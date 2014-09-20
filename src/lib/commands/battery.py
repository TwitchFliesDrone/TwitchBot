# coding: utf8

import requests, json

def battery():
	
	port = 3050
	
#	try:
	r = requests.get('http://localhost:' + str(port) + '/control/battery')
#	except:
#		return 'Error!'

	return 'Getting battery!'