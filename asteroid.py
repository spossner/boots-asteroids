from constants import *
from circleshape import *
import pygame

class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)

    def draw(self, surface: pygame.surface.Surface):
        pygame.draw.circle(surface, "white", self.position, self.radius, 2)    

    def update(self, dt: float):
        self.position += (self.velocity * dt)
