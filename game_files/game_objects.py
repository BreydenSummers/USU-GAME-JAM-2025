import pygame

TILE_SIZE = 8

class NonInteractiveObject:
    def __init__(self,sprite,row,column):
        self.sprite = pygame.image.load(sprite).convert_alpha()
        self.x = row * 8
        self.y = column * 8

    def draw(self,screen):
        self.sprite.blit(screen,(self.x,self.y))