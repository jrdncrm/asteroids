import pygame
from circleshape import *
from constants import *
from main import *
from bullets import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_timer = 0.0

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
            # sub-classes must override
            pygame.draw.polygon(screen, "white", self.triangle(),2)
    
    def rotate(self, dt):
        self.rotation += (PLAYER_TURN_SPEED * dt)

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.shoot_timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            if self.shoot_timer <= 0:
                self.shoot()
          
                

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_TURN_SPEED * dt
    
    def shoot (self):
        bullet = Bullet(self.position.x, self.position.y, SHOT_RADIUS, self.rotation)
        self.shoot_timer = PLAYER_SHOOT_TIMER
        
    


        