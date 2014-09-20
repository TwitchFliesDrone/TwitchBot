from src.config.config import *

commands = {
	'!test': {
		'limit': 30,
		'return': 'This is a test!'
	},

	'!randomemote': {
		'limit': 180,
		'argc': 0,
		'return': 'command'
	},

	'!wow': {
		'limit': 30,
		'argc': 3,
		'return': 'command'
	},

	'!turn': {
		'limit': 5,
		'argc': 1,
		'return': 'command'
	},
	
	'!takeoff': {
		'argc': 0,
		'limit': 10,
		'return': 'command'
	},

	'!land': {
		'argc': 0,
		'limit': 10,
		'return': 'command'
	}, 

	'!forward': {
		'argc': 0,
		'limit': 10,
		'return': 'command'
	}, 

	'!backward': {
		'argc': 0,
		'limit': 10, 
		'return': 'command'
	},

	'!battery': {
		'argc': 0, 
		'limit': 10,
		'return': 'command'
	}
}










for channel in config['channels']:
	for command in commands:
		commands[command][channel] = {}
		commands[command][channel]['last_used'] = 0
