import pygame

from config import parse_config_file

CONFIG = config.parse_config_file('main')

SCREEN_WIDTH = CONFIG['SCREEN']['width']
SCREEN_HEIGHT = CONFIG['SCREEN']['height']

FPS = CONFIG['FPS']['fps']

def main():
	fps_clock = pygame.time.Clock()
	debug = bool(CONFIG['DEBUG']['debug'])
	window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	while True:
		pygame.event
		fps_clock.tick(FPS)
