from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, SHOT_RADIUS)
        self.ttl = 1.7

    def draw(self, surface: pygame.surface.Surface):
        pygame.draw.circle(surface, COLOR_FG, self.position, self.radius, 2)    

    def update(self, dt: float):
        self.ttl -= dt
        if self.ttl <= 0:
            self.kill()
            return
        self.position += (self.velocity * dt)
