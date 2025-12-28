import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, AIRPLANE_RADIUS)
        self.rotation = 180
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (0,255,255), self.triangle(), 2)

    def moveVertical(self, dt):
        forward = pygame.Vector2(0, 1)
        self.position += forward * PLAYER_SPEED * dt

    def moveHorizontal(self, dt):
        right = pygame.Vector2(1, 0)
        self.position += right * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer > 0:
            return
        shot = Shot(self.position.x, self.position.y - AIRPLANE_RADIUS/2)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
        self.timer = PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        if self.timer > 0:
            self.timer -= dt
            if self.timer < 0:
                self.timer = 0
        if self.position.x < 0:
            self.position.x = SCREEN_WIDTH
        if self.position.x > SCREEN_WIDTH:
            self.position.x = 0
        if self.position.y < 0:
            self.position.y = SCREEN_HEIGHT
        if self.position.y > SCREEN_HEIGHT:
            self.position.y = 0
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.moveHorizontal(-dt)
        if keys[pygame.K_d]:
            self.moveHorizontal(dt)
        if keys[pygame.K_w]:
            self.moveVertical(- dt)
        if keys[pygame.K_s]:
            self.moveVertical(dt)
        if keys[pygame.K_SPACE]:
            self.shoot()