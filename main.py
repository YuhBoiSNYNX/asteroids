import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
def main():
    # init
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Asteroids")

    # clock
    clock = pygame.time.Clock()
    dt = 0


    #groups
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # containers
    Player.containers = [updateable, drawable]
    Asteroid.containers = [asteroids, updateable, drawable]
    AsteroidField.containers = [updateable]
    Shot.containers = [shots, updateable, drawable]

    # objects
    asteroidfield = AsteroidField()

    # player
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # is the game loop running flag. Used for closing the game.
    running = True
    # game loop
    while running:
        dt = clock.tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        updateable.update(dt)
        for obj in asteroids:
            if player.collision(obj):
                print("Game over!")
                running = False
            for shot in shots:
                if shot.collision(obj):
                    shot.kill()
                    obj.split()

        screen.fill((0, 0, 0))
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()