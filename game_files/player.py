import pygame
import os


assets_path = os.path.join(os.path.dirname(os.path.dirname( __file__ )), "assets")
print(assets_path)


class Player:
    def load_sprite_images(self, directory):
        sprites = []
        for sprite in os.listdir(os.path.join(assets_path, directory)):
            sprites.append(
                pygame.image.load(os.path.join(assets_path, directory, sprite)).convert_alpha()
            )
        return sprites

    def __init__(self):
        self.idle_animations = {
            "up" : self.load_sprite_images("ThisJohn_up")
        }
    
    def animate(self, surface, frame_number):
        current_sprite = self.idle_animations["up"][
            frame_number % len(self.idle_animations["up"])
        ]
        surface.blit(current_sprite, (0, 0))