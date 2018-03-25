#!/usr/bin/env python
#hello
import pygame, math, sys, random
from pygame.locals import *
from globalVars import *
from brick import *
from water import *
from tools import *

"""
This file handles level creation and animated tiles. The level is built
by a simple automata, so every tile is reachable.
"""

class level:
	#Initializing builds the level
	def __init__(self,levelSize):
		self.pos = (0,0)
		self.levelSize = levelSize
		self.windowSize = WINDOWSIZE
		self.surf = pygame.Surface(levelSize)
		self.waterSurf = waterTile(TILESIZE)
		self.floors = []
		self.walls = []
		self.xWalls = {}
		self.wallDixct = {}
		self.moves = self.getMoves()
		self.buildLevel()
		self.cleanSurf = self.surf
		self.eCount = 100#amount of enemies
		self.time = 0
		
	#determines how many moves the automata will make	
	def getMoves(self):
		x = self.levelSize[0]//TILESIZE[0]
		y = self.levelSize[1]//TILESIZE[1]
		return (x*y)*2
			
	def buildLevel(self):
		self.drawFloor()
		self.drawWater()
	
	#draws brick tile to level
	def drawBrick(self,x,y):
		self.surf.blit(BrickTile(TILESIZE).surf,(x,y))	
		return
	
	#gets next direction for automata, makes sure it stays within the level
	def getDirection(self,x,y):
		up = (x,y-TILESIZE[1])
		down = (x,y+TILESIZE[1])
		left = (x-TILESIZE[0],y)
		right = (x+TILESIZE[0],y)
		direction = random.choice([up,down,left,right])
		while direction[0] < 0 or direction[1] < 0 or direction[0] >= self.levelSize[0] or direction[1] >= self.levelSize[1]:
			direction = random.choice([up,down,left,right])	
		return direction	
		
	#creates level using simple automata
	def drawFloor(self):	
		x=self.levelSize[0]//2
		y=self.levelSize[1]//2
		for z in range(self.moves,0,-1):
			direction = self.getDirection(x,y)
			x,y = direction		
			self.drawBrick(x,y)
			if y == 0:
				rc = 32
				for b in range(TILESIZE[0]//2):
					pygame.draw.line(self.surf,(0,0,0),(x,b),(x+TILESIZE[0],b),1)
					rc -=1					
			self.floors.append(direction)								
		
	def drawWater(self,x=0,y=0):
		for x in range(0,self.levelSize[0],TILESIZE[0]):
			self.xWalls[x] = []
			for y in range(0,self.levelSize[1],TILESIZE[1]):
				if (x,y) not in self.floors:					
					self.surf.blit(self.waterSurf.surfs[self.waterSurf.surfC],(x,y))
					self.walls.append((x,y))
					self.xWalls[x].append((x,y))
				if (x,y-TILESIZE[1]) in self.floors:
					for b in range(TILESIZE[1]//2):
						pygame.draw.line(self.surf,(0,0,0),(x,b),(x+TILESIZE[0],b),1)
	
	#goes through each tile to see if its empty and fills it with water		
	def redrawWater(self,camera,dude):
		for wall in self.walls:
			rect = Rect(wall,TILESIZE)

			if dude.rect.center[0] > rect.center[0]:
				side = 'left'
				dist = camera.center[0] - rect.center[0]
			else:
				side = 'right'
				dist = rect.center[0] - dude.rect.center[0]
			if dist >= TILESIZE[0]//2:
				dist = TILESIZE[0]
			if inCamera(camera,rect):				
				self.surf.blit(self.waterSurf.surfs[self.waterSurf.surfC],wall)
				if (wall[0],wall[1]-TILESIZE[1]) in self.floors:
					for b in range(TILESIZE[1]//6):
						pygame.draw.line(self.surf,(0,0,25),(wall[0],wall[1]+b),(wall[0]+TILESIZE[0],wall[1]+b),1)
				if (wall[0]-TILESIZE[0],wall[1]) in self.floors:
					if side == 'left':
						for b in range(TILESIZE[1]//6):	
							pygame.draw.line(self.surf,(0,0,25),(wall[0]+b,wall[1]),(wall[0]+b,wall[1]+TILESIZE[1]),1)
					elif dude.rect.left > rect.left:
						if dude.rect.left-rect.left <= TILESIZE[0]//6:
							for b in range(dude.rect.left-rect.left):	
								pygame.draw.line(self.surf,(0,0,25),(wall[0]+b,wall[1]),(wall[0]+b,wall[1]+TILESIZE[1]),1)
						else:
							for b in range(TILESIZE[1]//6):	
								pygame.draw.line(self.surf,(0,0,25),(wall[0]+b,wall[1]),(wall[0]+b,wall[1]+TILESIZE[1]),1)
				if (wall[0]+TILESIZE[0],wall[1]) in self.floors and side=='right':
					for b in range(TILESIZE[1]//6):	
						pygame.draw.line(self.surf,(0,0,25),(wall[0]+TILESIZE[0]-b,wall[1]),(wall[0]+TILESIZE[0]-b,wall[1]+TILESIZE[1]),1)
											
	def updateLevel(self,camera,fpsn,dude):
		self.cleanSurf = self.surf.copy()
		self.time += fpsn
		if self.time >= 6:
			self.time = 0
			self.waterSurf.switchSurf()
			self.redrawWater(camera,dude)
		

