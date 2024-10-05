from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, SHOT_RADIUS)

    def draw(self, surface: pygame.surface.Surface):
        pygame.draw.circle(surface, COLOR_FG, self.position, self.radius, 2)    

    def update(self, dt: float):
        self.position += (self.velocity * dt)
