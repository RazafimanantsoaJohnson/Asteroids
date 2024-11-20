import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidField import AsteroidField

def main():
    print("Starting asteroids!")
    pygame.init()
    screen= pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock= pygame.time.Clock()
    dt= 0
    updatables= pygame.sprite.Group()
    drawables= pygame.sprite.Group()
    asteroids= pygame.sprite.Group()
    
    Player.containers= (updatables, drawables) 
    Asteroid.containers= (asteroids,updatables,drawables)
    
    player= Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_obj= Asteroids(0,0,300)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill("black")
        
        for updatable in updatables:
            updatable.update(dt)
        
        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()
        dt= clock.tick(60)/1000

if __name__=="__main__":
    main()
