import pygame

# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def check_for_collision(self, circle):
        rsum = self.radius + circle.radius
        distance = self.position.distance_to(circle.position)
        return rsum > distance

    def check_for_collision2(self, plane):
        a = plane.triangle()[0]
        b = plane.triangle()[1]
        c = plane.triangle()[2]
        
        distance1 = self.position.distance_to(a)
        distance1_2 = self.position.distance_to( ((a.x+b.x)/2, (a.y+b.y)/2) )
        distance2 = self.position.distance_to(b)
        distance2_3 = self.position.distance_to( ((b.x+c.x)/2, (b.y+c.y)/2) )
        distance3 = self.position.distance_to(c)
        distance1_3 = self.position.distance_to( ((a.x+c.x)/2, (a.y+c.y)/2) )

        return (self.radius > distance1 or self.radius > distance1_2 or self.radius > distance2 or self.radius > distance2_3 or self.radius > distance3 or self.radius > distance1_3)