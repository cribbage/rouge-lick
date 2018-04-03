import sys
import pygame
from pygame.locals import *

from config import Config

FPS = CONFIG['FPS'].getint('fps')

def main():
	fps_clock = pygame.time.Clock()
	debug = CONFIG['DEBUG'].getboolean('debug')
	window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), NOFRAME)
	config = Config('main')
	config['test'] = 'test1'
	config.save()
	sys.exit()
		
	while True:
		events = pygame.event.get()
		fps_clock.tick(FPS)
