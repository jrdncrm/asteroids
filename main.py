# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *

def main():
	pygame.init()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	print("Starting asteroids!")
	print(f'Screen width: {SCREEN_WIDTH}')
	print(f'Screen height: {SCREEN_HEIGHT}')
	clock = pygame.time.Clock()
	dt = 0
	
	updateables = pygame.sprite.Group()
	drawables = pygame.sprite.Group()
	destroyables = pygame.sprite.Group()
	shots = pygame.sprite.Group()

	AsteroidField.containers = (updateables)
	Asteroid.containers = (updateables, drawables, destroyables)
	Player.containers = (updateables, drawables)
	Bullet.containers = (updateables, drawables, shots)

	player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()

	while True:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return

		screen.fill("black")
		for drawable in drawables:
			drawable.draw(screen)
		updateables.update(dt)
		for destroyable in destroyables:
			if destroyable.collision_check(player):
				print("Game Over!")
				return
				sys.exit()
		pygame.display.flip()


		clock.tick(60)
		dt = clock.get_time() / 1000
if __name__ == "__main__":
    main()

