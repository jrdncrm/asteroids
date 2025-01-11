# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from circleshape import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting asteroids!")
	print(f'Screen width: {SCREEN_WIDTH}')
	print(f'Screen height: {SCREEN_HEIGHT}')
	clock = pygame.time.Clock()
	dt = 0
	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	updateables = pygame.sprite.Group()
	drawables = pygame.sprite.Group()
	Player.containers = (updateables, drawables)
	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill("black")
		drawables.draw(screen)
		updateables.update(dt)
		pygame.display.flip()


		clock.tick(60)
		dt = clock.get_time() / 1000
if __name__ == "__main__":
    main()

