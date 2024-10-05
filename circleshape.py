import pygame
from constants import *

class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, radius: float):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, surface: pygame.surface.Surface):
        # sub-classes must override
        pass

    def update(self, dt: float):
        # sub-classes must override
        pass
    
    def check_collision(self, other):
        return self.position.distance_to(other.position) <= self.radius + other.radius

    def check_wrap_around(self):
        if self.position.x < 0:
            self.position.update(self.position.x + SCREEN_WIDTH, self.position.y)
        elif self.position.x > SCREEN_WIDTH:
            self.position.update(self.position.x - SCREEN_WIDTH, self.position.y)
        if self.position.y < 0:
            self.position.update(self.position.x, self.position.y + SCREEN_HEIGHT)
        elif self.position.y > SCREEN_HEIGHT:
            self.position.update(self.position.x, self.position.y - SCREEN_HEIGHT)
