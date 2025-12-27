import pygame
import random
from constants import *
from planes import Airplane

class PlaneFactory(pygame.sprite.Sprite):
    paths = [1, 2, 3, 4]
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0

    def spawn(self, path):
        if path == 1:
            position = pygame.Vector2(random.uniform(0.6, 1.1) * SCREEN_WIDTH, -AIRPLANE_RADIUS)  # Right side
        elif path == 2:
            position = pygame.Vector2(random.uniform(-0.1, 0.4) * SCREEN_WIDTH, -AIRPLANE_RADIUS) # Left side
        elif path == 3:
            position = pygame.Vector2(random.uniform(0.3, 0.7) * SCREEN_WIDTH, -AIRPLANE_RADIUS)  # Center top
        elif path == 4:
            position = pygame.Vector2(random.uniform(0.3, 0.7) * SCREEN_WIDTH, -AIRPLANE_RADIUS)  # Center top

        airplane = Airplane(position.x, position.y, path)
    
    def update(self, dt):
        self.spawn_timer += dt
        if self.spawn_timer > AIRPLANE_SPAWN_INTERVAL:
            self.spawn_timer = 0.0

            path = random.choice(self.paths)
            self.spawn(path)
            

