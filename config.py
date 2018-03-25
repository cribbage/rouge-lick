import configparser

def parse_config_file(config_file):
	config = configparser.ConfigParser()
	config.read(config_file)
	return config
