import pygame, random

from Constants import *

class Fruit:
	def __init__(self, surface):
		self.position = [random.randint(1, GRID[0]), random.randint(1, GRID[1])]
		self.texture = TEXTURES[random.choice(['APPLE', 'BANANA', 'ORANGE'])]
		self.surface = surface

	def draw(self):
		texture = pygame.image.load(self.texture)
		self.surface.blit(texture, (self.position[0] * PIXEL_OFFSET, self.position[1] * PIXEL_OFFSET))

	def spawn(self, snake):
		possiblePositions = []
		
		for i in range(0, GRID[0] + 1):
			for n in range(0, GRID[1] + 1):
				if not [i, n] in snake.body:
					possiblePositions.append([i, n])

		self.position = random.choice(possiblePositions)
		self.texture = TEXTURES[random.choice(['APPLE', 'BANANA', 'ORANGE'])]