import os
from configparser import ConfigParser

CONFIG_DIR = '.'

class Config:
	def __init__(self, config_file):
		self.file_name = config_file
		self.file_path = os.path.join(CONFIG_DIR, self.file_name)
		self.data = ConfigParser()
		self.data.read(self.file_path)
		
	def __getitem__(self, key):
		try:
			return self.data[key]
		except KeyError:
			print('Config file section title [{}] does not exist!'.format(key))
		
	def __setitem__(self, key, value):
		try:
			self.data[key] = value
		except KeyError:
			print('Config file section title [{}] does not exist!'.format(key))
			
	def has_section(self, section):
		with open(self.file_path, 'r') as f:
			for line in f:
				if '[{}]'.format(section) in line:
					return True
		return False
		
	def save(self):
		with open(self.file_path, 'w') as f:
			self.data.write(f)


def test():
	c = Config('settings')
	
test()
