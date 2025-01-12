from circleshape import *
import random   
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        

    def draw(self, screen): 
        pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else: 
            random_angle = random.randint(20,50)
            split1 = self.velocity.rotate(random_angle)
            split2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asteroid1.velocity = split1 * 1.2
            new_asteroid2.velocity = split2 * 1.2

            