import pygame
from circleshape import CircleShape
from constants import *
from shot import Shot

class Player(CircleShape):

    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        # rotation is not a typical property, it's a property that is defined and used in our Sprite parent to draw our 
        # visual element with the rotation we want.
        self.rotation= 0
        self.timer= 0       # a variable that will be set to a value at each shot and checked if >0 (to prevent us from shooting too many times)

    def  triangle(self):
        forward= pygame.Vector2(0,1).rotate(self.rotation)
        right= pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius/1.5
        a= self.position + forward * self.radius
        b= self.position - forward * self.radius - right
        c= self.position - forward * self.radius + right

        return [a,b,c]
    
    def draw(self,screen):
        pygame.draw.polygon(screen,"white",self.triangle(),2)


    def update(self,dt):
        keys= pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_a]:
            self.rotate(dt* -1) 

        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

    def shoot(self):
        if self.timer > 0:
            return
        
        shot= Shot(self.position.x, self.position.y)
        shot.velocity= pygame.Vector2(0,1)
        shot.velocity= shot.velocity.rotate(self.rotation)
        shot.velocity= shot.velocity * PLAYER_SHOT_SPEED

        self.timer= PLAYER_SHOOT_COOLDOWN


    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt
    def rotate(self,dt):
        self.rotation+= PLAYER_TURN_SPEED * dt
