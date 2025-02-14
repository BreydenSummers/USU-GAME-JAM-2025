import pygame
from pygame._sdl2 import Window
from random import randint
import os
from game_files.player import Player
from game_files.scene import Scene
from game_files.ui_objects import *


pygame.init()
assets_path = os.path.join(os.path.dirname( __file__ ), "..", "Assets")

display = pygame.display.set_mode((1, 1))
player = Player()

#menu = Scene(os.path.join(assets_path,"Background/map.png"),400,300)
#menu.add_ui_object(RectButton(200,150,100,50,(200,200,200),print,text="Start"))

class Game:
    def __init__(self, window_size = (400, 300), max_framerate = 30):
        self.window = pygame.display.set_mode((window_size), pygame.NOFRAME)
        self.frame_timer = pygame.time.Clock()
        self.max_framerate = max_framerate

        self.sdl_window = Window.from_display_module() 
        self.running = True
        self.frame_count = 0

        self.map = pygame.image.load(os.path.join(assets_path, "Background/map.png")).convert()


    def start_systems(self):
        pygame.key.set_repeat(10, 10)

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
            
            pressed_keys = pygame.key.get_pressed()
            
            if pressed_keys[pygame.K_w]:
                player.move("up", self.frame_count)
            if pressed_keys[pygame.K_s]:
                player.move("down", self.frame_count)
            if pressed_keys[pygame.K_a]:
                player.move("left", self.frame_count)
            if pressed_keys[pygame.K_d]:
                player.move("right", self.frame_count)
            if pressed_keys[pygame.K_ESCAPE]:
                self.running = False
            if pressed_keys[pygame.K_p]:
                self.set_window_position(
                    (200, 200), (600, 400)
                )


    def update_physics(self):
        pass

    def update_display(self):
        self.window.fill((255, 255, 255))

        self.window.blit(self.map, (0, 0))

        player.draw_to_surface(self.window, self.frame_count)

        pygame.display.update()
        self.frame_count += 1
        self.frame_timer.tick(self.max_framerate)

    def run_game(self):
        self.start_systems()

        while self.running:
            self.handle_events()

            self.update_physics()

            self.update_display()


if __name__ == "__main__":
    game = Game(
        window_size=(400, 300)
    )
    game.run_game()