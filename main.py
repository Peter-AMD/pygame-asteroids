import sys
import pygame

from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_clock = pygame.time.Clock()

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    player_instance = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    Asteroid.containers = (asteroids, updatables, drawables)                                                                                                                                                                          
    AsteroidField.containers = (updatables)
    AsteroidField()
    Shot.containers = (updatables, drawables, shots)

    dt = 0

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updatables.update(dt)
        for asteroid in asteroids:
            if asteroid.detect_collision(player_instance):
                print("Game over!")
                sys.exit()
        screen.fill("black")

        for dr in drawables:
            dr.draw(screen)

        pygame.display.flip()
        # converts ms to s, limit framerate to 60 FPS
        dt = game_clock.tick(60) / 1000



if __name__ == "__main__":
    main()
