# coding: utf8

import requests, json

def forward():
	
	port = 3050
	
#	try:
	r = requests.get('http://localhost:' + str(port) + '/control/forward')
#	except:
#		return 'Error!'

	return 'Moving forward!'