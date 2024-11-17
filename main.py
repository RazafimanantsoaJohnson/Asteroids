import pygame
from constants import *

def main():
    print("Starting asteroids!")
    pygame.init()
    pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return
        while True:
            pygame.display.flip()

if __name__=="__main__":
    main()
