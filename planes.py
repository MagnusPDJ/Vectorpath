import pygame
from constants import *
from circleshape import CircleShape
from shot import Shot

class Airplane(CircleShape):
    def __init__(self, x, y, path):
        super().__init__(x, y, AIRPLANE_RADIUS)
        self.rotation = 0
        self.timer = ENEMY_SHOOT_COOLDOWN
        self.debugTimer = 0.0
        self.path = path
        self.tx = -1.5
        self.ty = -1.5

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255,0,0), self.triangle(), 2)
    
    def update(self, dt):
        if self.timer > 0:
            self.timer -= dt
            if self.timer < 0:
                self.timer = 0

#        if self.debugTimer > 0:
#            self.debugTimer -= dt
#            if self.debugTimer < 0:
#                self.debugTimer = 0
#        if self.debugTimer <= 0:
#            print(self.position)
#            self.debugTimer = 0.3
        self.shoot()
        self.move(dt)

        if self.position.y > 720:
            self.kill()
        
    def shoot(self):
        if self.timer > 0:
            return
        shot = Shot(self.position.x, self.position.y + AIRPLANE_RADIUS/2)
        shot.player_shot = False
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * ENEMY_SHOOT_SPEED
        self.timer = ENEMY_SHOOT_COOLDOWN

    def move(self, dt):
        if self.path == 1:
            self.position += pygame.Vector2(-self.xfunction(dt), self.yfunction(dt))
        elif self.path == 2:
            self.position += pygame.Vector2(self.xfunction(dt), self.yfunction(dt))
        elif self.path == 3:
            self.position += pygame.Vector2(-self.xpath3(dt), self.yfunction(dt))
        elif self.path == 4:
            self.position += pygame.Vector2(self.xpath3(dt), self.yfunction(dt))

    def xfunction(self, dt):
        x = 4
        self.tx += dt
        return x

    def yfunction(self, dt):
        y = 3 * pow(self.ty, 2)
        self.ty += dt
        return y
    
    def xpath3(self, dt):
        x = 2 * 2 * self.tx
        self.tx += dt
        return x
