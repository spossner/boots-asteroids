import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *
from explosion import *

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
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    Explosion.containers = (updatable, drawable)
    AsteroidField.containers = (updatable)

    field = AsteroidField()
    player = Player(x, y)

    font = pygame.font.SysFont(None, 24)

    while running:
        # poll for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pygame.QUIT event means the user clicked X to close your window
                running = False

        # fill the screen with black to wipe away anything from last frame
        screen.fill(COLOR_BG)

        # Update the updateables passing the passed time since last loop (delta time)
        for thing in updatable:
            thing.update(dt)

        # check collision with asteroids -> game over..
        for asteroid in asteroids:
            killed = False
            for s in shots:
                if asteroid.check_collision(s): # asteroid was hit by shot
                    score = max(ASTEROID_KINDS - (asteroid.radius // ASTEROID_MIN_RADIUS), 0) + 1
                    player.add_score(score*10)
                    s.kill()
                    asteroid.split()
                    killed = True
                    break

            if not killed and asteroid.check_collision(player):
                print("Game over!")
                print(f"Score: {player.score}")
                running = False



        # draws the drawable things onto the screen
        for thing in drawable:
            thing.draw(screen)

        # draw score
        
        img = font.render(f"Score: {player.score}", True, "#fef08a")
        screen.blit(img, (20, 20))

        # flip() the display to put your work on screen
        pygame.display.flip()

        dt = clock.tick(60) / 1000 # limits FPS to 60

    pygame.quit()


if __name__ == "__main__":
    main()
