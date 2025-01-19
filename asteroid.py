import pygame
from circleshape import CircleShape
from constants import *
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self,screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,2)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            vector1 =self.velocity.rotate(random_angle)
            vector2 = self.velocity.rotate(-random_angle)
            radius = self.radius - ASTEROID_MIN_RADIUS
            Asteroid_1=Asteroid(self.position.x,self.position.y,radius)
            Asteroid_2=Asteroid(self.position.x,self.position.y,radius)
            Asteroid_1.velocity = vector1 * 1.2
            Asteroid_2.velocity = vector2 * 1.2



