import pygame

TILE_SIZE = 8

class Scene:
    def __init__(self, image, w, h):
        self.image = pygame.image.load(image)
        self.image.convert()

        self.objects = []
        self.surface = pygame.Surface((w, h))
        self.image.blit(self.surface, (0, 0))

        self.map = [[0 for _ in range(h/TILE_SIZE)] for _ in range(w/TILE_SIZE)]

    def add_map_object(self, obj, row, column):
        self.map[row][column] = obj
        self.map[row][column].draw(self.surface)


    def add_ui_object(self, obj):
        self.objects.append(obj)
        obj.draw(self.surface)

    def draw(self,screen):
        self.surface.blit(screen, (0, 0))