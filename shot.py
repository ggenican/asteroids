from circleshape import *
from constants import *

class Shot(CircleShape):
    def __init__(self, x, y, player_rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.move(player_rotation)
    
    def move(self, player_rotation):
        self.velocity = pygame.Vector2(0, 1).rotate(player_rotation) * PLAYER_SHOOT_SPEED

    def rotate(self, player_rotation):
        self.rotation = player_rotation

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt