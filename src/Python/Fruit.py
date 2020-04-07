import pygame, random

from Constants import *

class Fruit:
	def __init__(self, surface):
		self.position = [random.randint(1, GRID[0]), random.randint(1, GRID[1])]
		self.surface = surface

	def draw(self):
		pygame.draw.rect(self.surface, RED, pygame.Rect(self.position[0] * PIXEL_OFFSET, self.position[1] * PIXEL_OFFSET, PIXEL_OFFSET, PIXEL_OFFSET))

	def spawn(self, snake):
		possiblePositions = []
		
		for i in range(0, GRID[0] + 1):
			for n in range(0, GRID[1] + 1):
				if not [i, n] in snake.body:
					possiblePositions.append([i, n])

		self.position = random.choice(possiblePositions)