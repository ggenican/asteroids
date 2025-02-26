import random
from circleshape import *
from constants import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        random_angle = random.uniform(20, 50)
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        new_asteroid1 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)
        new_asteroid2 = Asteroid(self.position[0], self.position[1], self.radius - ASTEROID_MIN_RADIUS)

        new_asteroid1.velocity = self.velocity.rotate(random_angle) * 1.2
        new_asteroid2.velocity = self.velocity.rotate(-random_angle) * 1.2
    
    def collision(self, object):
        if self.position.distance_to(object.position) < self.radius + object.radius:
            self.split()
            object.kill()