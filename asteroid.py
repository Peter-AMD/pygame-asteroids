import pygame

from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(surface=screen, width=2, center=self.position, radius=self.radius, color="white")
    
    def update(self, dt):
        self.position += self.velocity * dt