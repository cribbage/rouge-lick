import pygame, sys
from pygame.locals import *

pygame.init()

class Engine:
	def __init__(self):
		handle_events()
		update_objects()
		render()
		
	def run(self):
		while True:
			events = pygame.event.get()
