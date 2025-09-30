import pygame
import os

dir = os.getcwd()

class player:
    def __init__(self, x, y, width, height, speed, image):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        self.image = image
        self.rect = (x,y,width,height)

    def get_character(self):
        image1 = pygame.image.load(self.image).convert_alpha()
        character = pygame.transform.smoothscale(image1,(self.width,self.height))

        return image1, character

    def Spawn_Player(self, character, x, y):
        characterFrame = character.get_rect(topleft=(x,y))

        return characterFrame
    
    def change_image(self, x, y, image):
        self.image = f"{dir}{image}"
        newimage = pygame.image.load(self.image).convert_alpha()
        character = pygame.transform.smoothscale(newimage,(self.width,self.height))
        characterFrame = character.get_rect(topleft=(x, y))

        return character, characterFrame

    def move(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_a]:
            self.x -= self.speed

        if keys[pygame.K_d]:
            self.x += self.speed
        
        if keys[pygame.K_w]:
            self.y -= self.speed

        if keys[pygame.K_s]:
            self.y += self.speed
        
        self.update()
        
    def update(self):
        self.rect = (self.x, self.y, self.width, self.height)
