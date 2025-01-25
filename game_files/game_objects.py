import pygame

TILE_SIZE = 8

class NonInteractiveObject:
    def __init__(self,sprite,row,column):
        self.sprite = pygame.image.load(sprite).convert_alpha()
        self.x = row * TILE_SIZE
        self.y = column * TILE_SIZE

    def draw(self,screen):
        self.sprite.blit(screen,(self.x,self.y))

class InteractiveObject:
    def __init__(self,sprite,row,column):
        self.sprite = pygame.image.load(sprite).convert_alpha()
        self.x = row * TILE_SIZE
        self.y = column * TILE_SIZE

    def draw(self,screen):
        self.sprite.blit(screen,(self.x,self.y))

    