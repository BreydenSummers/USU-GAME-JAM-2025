import pygame
from pygame._sdl2 import Window
from random import randint
import os

class Game:
    def __init__(self, window_size = (400, 300), max_framerate = 30):
        self.window = pygame.display.set_mode((window_size), pygame.NOFRAME)
        self.frame_timer = pygame.time.Clock()
        self.max_framerate = max_framerate

        self.sdl_window = Window.from_display_module()
        self.running = True

        #$self.level_1_bmp = pygame.image.load(os.path.join("__file__"))


    def window_size(self):
        return self.window.get_size()
    
    def set_window_position(self, top_left, size=0):
        self.sdl_window.position = top_left
        if size == 0:
            size = self.window_size()
        self.window = pygame.display.set_mode(size, pygame.NOFRAME)
    

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return 0
            #print(event)

    def update_physics(self):
        pass

    def update_display(self):
        self.window.fill((255, 255, 255))

        pygame.display.update()
        self.frame_timer.tick(self.max_framerate)

    def run_game(self):
        while self.running:
            self.handle_events()

            self.update_physics()

            self.update_display()


if __name__ == "__main__":
    game = Game(
        window_size=(120, 80)
    )
    game.run_game()