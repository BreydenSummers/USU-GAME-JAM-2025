import pygame

TILE_SIZE = 8

class Scene:
    def __init__(self, image, w, h):
        self.image = pygame.image.load(image)
        self.image.convert()

        self.objects = []
        self.surface = pygame.Surface((w, h))
        self.surface.blit(self.image, (0, 0))

        self.map = [[0 for _ in range(int(h/TILE_SIZE))] for _ in range(int(w/TILE_SIZE))]

    def add_map_object(self, obj, row, column):
        self.map[row][column] = obj
        self.map[row][column].draw(self.surface)

    def check_occupied(self,row,column):
        if self.map[row][column] is not None:
            return True
        else:
            return False

    def add_ui_object(self, obj):
        self.objects.append(obj)
        obj.draw(self.surface)

    def draw(self,screen):
        screen.blit(self.surface, (0, 0))