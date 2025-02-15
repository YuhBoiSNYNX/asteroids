import circleshape
import constants
import pygame
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return


        random_angle = random.uniform(20, 50)

        v1 = self.velocity.rotate(random_angle)
        v2 = self.velocity.rotate(-random_angle)


        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        new_astroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_astroid1.velocity = v1 * 1.2
        new_astroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_astroid2.velocity = v2 * 1.2
