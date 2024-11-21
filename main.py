import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidField import AsteroidField
from shot import Shot

def main():
    print("Starting asteroids!")
    pygame.init()
    screen= pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock= pygame.time.Clock()
    dt= 0
    updatables= pygame.sprite.Group()
    drawables= pygame.sprite.Group()
    asteroids= pygame.sprite.Group()
    shots= pygame.sprite.Group()
    
    Player.containers= (updatables, drawables) 
    Asteroid.containers= (asteroids,updatables,drawables)
    AsteroidField.containers= (updatables)
    Shot.containers= (updatables,shots,drawables)

    player= Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    #asteroid_obj= Asteroid(0,0,300)
    asteroid_field= AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")

        for asteroid in asteroids:
            if asteroid.check_collide(player):
                print("Game over BG")
                return 
            
            for shot in shots:
                if asteroid.check_collide(shot):
                    shot.kill()
                    asteroid.split()
               
        for updatable in updatables:
            updatable.update(dt)
        
        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()
        dt= clock.tick(60)/1000

if __name__=="__main__":
    main()
