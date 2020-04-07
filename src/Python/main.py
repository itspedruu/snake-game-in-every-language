import sys, pygame, threading, time, random, math

from Constants import *
from Snake import Snake
from Fruit import Fruit

pygame.init()
pygame.font.init()

font = pygame.font.SysFont("Comic Sans MS", 30)

# Window 
size = width, height = (GRID[0] + 1)  * PIXEL_OFFSET, (GRID[1] + 1) * PIXEL_OFFSET
pygame.display.set_caption('Snake Game in Every Language')
surface = pygame.display.set_mode(size)

# Game Variables
status = ''
snake = Snake(surface)
fruit = Fruit(surface)

def draw():
	# Fills screen with black
	surface.fill(BLACK)

	text_surface = None

	# Draws elements
	if status == '':
		snake.draw()
		fruit.draw()
	elif status == 'lose':
		text_surface = font.render('Game Over!', 1, RED)
	elif status == 'win':
		text_surface = font.render('You won!', 1, GREEN)

	if text_surface:
		surface.blit(text_surface, ((width - text_surface.get_width()) // 2, (height - text_surface.get_height()) // 2))

	# Updates screen
	pygame.display.flip()

def gameUpdate():
	global status

	snake.update()

	if snake.hasCollidedWith([fruit.position]):
		snake.eat(fruit)
	
	if snake.hasCollidedWithItself():
		status = 'lose'
	
	if snake.hasReachedMaxLength():
		status = 'win'

	draw()

def restart():
	global status, snake, fruit

	status = ''
	snake = Snake(surface)
	fruit = Fruit(surface)

def handleKeys(key):
	if key == pygame.K_UP:
		snake.moveUp()
	elif key == pygame.K_DOWN:
		snake.moveDown()
	elif key == pygame.K_LEFT:
		snake.moveLeft()
	elif key == pygame.K_RIGHT:
		snake.moveRight()
	elif key == pygame.K_r:
		restart()

while 1:
	# Pygame Events
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			handleKeys(event.key)

	# Updates content of the game
	gameUpdate()

	# Tick update
	time.sleep(1 / TICKS)