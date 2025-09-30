import pygame
import random as rand
import os

dir = os.getcwd()

def spawn_Place(w,h):
    Spawn_width = rand.randint(0,w) # Spawn place of items across x
    Spawn_height = rand.randint(0,h) # Spawn place of items across y

    return Spawn_width, Spawn_height

class Items:
    def __init__(self, width, height, image):
        self.width = width
        self.height = height
        self.image = image

    def get_Item(self):
        image1 = pygame.image.load(f"{dir}\images\\{self.image}").convert_alpha()
        item = pygame.transform.smoothscale(image1,(self.width,self.height))
        
        return item
    
    def spawn(self, x, y):
        item = self.get_Item()
        itemFrame = item.get_rect(center=(x,y))

        return itemFrame
    
class ExplosionBomb:
    def __init__(self, width, height, image):
        self.width = width
        self.height = height
        self.image = image

    def get_ExplosionBomb(self):
        self.image = f'{dir}\images\{"ExplosionBomb.png"}'
        image1 = pygame.image.load(f'{self.image}').convert_alpha()
        bomb = pygame.transform.smoothscale(image1,(self.width,self.height))

        return bomb
    
    def get_explosion(self, width, height):
        self.image = f'{dir}\images\{"Explosion.png"}'
        image1 = pygame.image.load(f'{self.image}').convert_alpha()
        explosion = pygame.transform.smoothscale(image1,(width,height))

        return explosion
    
    def spawn(self, x, y):
        explosionBomb = self.get_ExplosionBomb()
        explosionBombFrame = explosionBomb.get_rect(center=(x,y))

        return explosionBombFrame
    
    def spawn_explosion(self, x, y, width, height):
        explosion = self.get_explosion(width, height)
        explosionFrame = explosion.get_rect(center=(x,y))

        return explosionFrame