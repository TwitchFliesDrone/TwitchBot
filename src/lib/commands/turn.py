# coding: utf8

import requests, json

def turn(args):
	direction = args[0]
	port = 3050
	
	if (direction != "right") and (direction != "left"):
		return
	r = requests.get('http://localhost:' + str(port) + '/control/turn-' + direction)


	return 'Turned!'
