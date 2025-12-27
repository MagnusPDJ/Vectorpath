import pygame
from constants import *
from planes import Airplane
from planefactory import PlaneFactory
from player import Player
from shot import Shot
from score import Score

def main():
    pygame.init()
    clock = pygame.time.Clock()
    dt = 0

    pygame.display.quit()
    pygame.display.set_caption("Vectorpath")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    planes = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    PlaneFactory.containers = updatable
    Airplane.containers = updatable, drawable, planes
    Player.containers = updatable, drawable
    Shot.containers = updatable, drawable, shots
    Score.containers = updatable, drawable
    
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT - 100)
    planefactory = PlaneFactory()
    score = Score()


    while True: 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        for update in updatable:
            update.update(dt)
        
        for plane in planes:
            if plane.check_for_collision2(player):
                score.endscreen(screen)
                pygame.display.update()
                while True:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            exit()
                        if event.type == pygame.KEYDOWN:
                            if pygame.key.name(event.key) == "n":
                                print("Goodbye")
                                exit()
                            if pygame.key.name(event.key) == "y":
                                main() 
            for shot in shots:
                if shot.player_shot:
                    if plane.check_for_collision(shot):
                        shot.kill()
                        plane.kill()
                        score.add_points()
                else:
                    if shot.check_for_collision2(player):
                        shot.kill()
                        score.endscreen(screen)
                        pygame.display.update()
                        while True:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    exit()
                                if event.type == pygame.KEYDOWN:
                                    if pygame.key.name(event.key) == "n":
                                        print("Goodbye")
                                        exit()
                                    if pygame.key.name(event.key) == "y":
                                        main() 


        screen.fill((0,0,0))        

        for draw in drawable:
            draw.draw(screen)
        
        pygame.display.flip()

        dt = clock.tick(60) / 1000




if __name__ == "__main__":
    print("Starting Vectorpath!")
    main()