import os

from config import Config

class Log:
	config = Config('settings')
	logs = config['DEBUG']['log_to'].split(', ')
		
	def write_console(msg):
		print(msg)
		
	def write_file(msg):
		with open(Log.config['DEBUG']['log_file'], 'a') as f:
			f.write(msg+'\n')
			
	def write_game(msg):
		pass
	
	def write(msg):
		for log_to in Log.logs:
			try:
				exec('Log.write_{function_name}("{msg}")'.format(
						function_name=log_to,
						msg=msg
					)
				)
			except AttributeError:
				print('Error in executing log functions! Check log settings.')
			
