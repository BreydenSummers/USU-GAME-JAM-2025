import pygame

class Scene:
    def __init__(self,image,w,h):
        self.image = pygame.image.load(image)
        self.image.convert()
        self.map = []
        self.objects = []
        for i in range(h/10):
            self.map.append([None for n in range(w/10)])
        self.surface = pygame.Surface((w,h))
        self.image.blit(self.surface,(0,0))

    def add_map_object(self,obj,row,column):
        self.map[row][column] = obj
        self.map[row][column].draw(self.surface)


    def add_ui_object(self,obj):
        self.objects.append(obj)
        obj.draw(self.surface)

    def draw(self,screen):
        self.surface.blit(screen,(0,0))