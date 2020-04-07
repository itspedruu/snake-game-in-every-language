import pygame

from Constants import *

class Snake:
	def __init__(self, surface):
		self.body = [[0, 0]]
		self.surface = surface
		self.speed = [0, 0]

	def draw(self):
		for position in self.body:
			pygame.draw.rect(self.surface, GREEN, pygame.Rect(position[0] * PIXEL_OFFSET, position[1] * PIXEL_OFFSET, PIXEL_OFFSET, PIXEL_OFFSET))

	def update(self):
		currentPosition = self.body[0].copy()

		currentPosition[0] += self.speed[0]
		currentPosition[1] += self.speed[1]

		if currentPosition[0] > GRID[0]:
			currentPosition[0] = 0
		elif currentPosition[0] < 0:
			currentPosition[0] = GRID[0]
		elif currentPosition[1] > GRID[1]:
			currentPosition[1] = 0
		elif currentPosition[1] < 0:
			currentPosition[1] = GRID[1]

		self.body.pop()
		self.body.insert(0, currentPosition)

	def addBody(self):
		self.body.append([self.body[-1][0] - self.speed[0], self.body[-1][1] - self.speed[1]])

	def eat(self, fruit):
		self.addBody()

		fruit.spawn(self)

	def moveLeft(self):
		self.speed = [-1, 0]

	def moveRight(self):
		self.speed = [1, 0]

	def moveUp(self):
		self.speed = [0, -1]

	def moveDown(self):
		self.speed = [0, 1]

	def hasCollidedWith(self, body):
		for position in body:
			if position == self.body[0]:
				return True

		return False

	def hasCollidedWithItself(self):
		return self.hasCollidedWith(self.body[1:])

	def hasReachedMaxLength(self):
		return len(self.body) == GRID[0] ** 2