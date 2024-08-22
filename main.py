import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from shot import Shot
from asteroidfield import AsteroidField


def main():
    pygame.init()

    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (updatable, drawable, asteroids)

    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Shot.containers = (shots, updatable, drawable)

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0.0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for updateObj in updatable:
            updateObj.update(dt)

        screen.fill((0, 0, 0))

        for drawObj in drawable:
            drawObj.draw(screen)

        for asteroidObj in asteroids:
            for shotObj in shots:
                if shotObj.collision(asteroidObj):
                    asteroidObj.split()
                    shotObj.kill()

            if player.collision(asteroidObj):
                print("Game Over")
                sys.exit(1)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
