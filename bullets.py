
from circleshape import *
from constants import *
from player import *

class Bullet(CircleShape):
    def __init__(self, x, y, radius, shot_direction):
        super().__init__(x, y, radius)
        self.velocity = pygame.Vector2(0, 1).rotate(shot_direction) * PLAYER_SHOOT_SPEED
        

    def draw(self, screen): 
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), SHOT_RADIUS, 2)

    def update(self, dt):
        self.position += self.velocity * dt