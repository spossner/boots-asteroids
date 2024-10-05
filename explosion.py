from circleshape import *
from constants import *
import random

class Explosion(CircleShape):
    def __init__(self, x: float, y: float):
        super().__init__(x, y, EXPLOSION_RADIUS)
        self.velocity = pygame.Vector2(0, 1).rotate(random.randint(0, 360)) * random.randint(EXPLOSION_MIN_SPEED, EXPLOSION_MAX_SPEED)
        self.ttl = random.randint(50, 400) / 1000
        self.color = random.choice(EXPLOSION_COLORS)

    def draw(self, surface: pygame.surface.Surface):
        pygame.draw.circle(surface, self.color, self.position, self.radius, 2)    

    def update(self, dt: float):
        self.ttl -= dt
        if self.ttl <= 0:
            self.kill()
            return
        self.position += (self.velocity * dt)
