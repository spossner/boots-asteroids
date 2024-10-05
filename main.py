import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    running = True

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)

    field = AsteroidField()
    player = Player(x, y)

    while running:
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked X to close your window
                running = False

        # fill the screen with black to wipe away anything from last frame
        screen.fill("black")

        # RENDER YOUR GAME HERE
        for thing in updatable:
            thing.update(dt)

        for thing in drawable:
            thing.draw(screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        dt = clock.tick(60) / 1000 # limits FPS to 60

    pygame.quit()


if __name__ == "__main__":
    main()
