import pygame
import os

TILE_SIZE = 32

assets_path = os.path.join(os.path.dirname(os.path.dirname( __file__ )), "Assets")
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
            "up" : self.load_sprite_images("player_sprites/up"),
            "down" : self.load_sprite_images("player_sprites/down"),
            "left" : self.load_sprite_images("player_sprites/left"),
            "right" : self.load_sprite_images("player_sprites/right")
        }
        self.position = [0, 0]
        self.facing = "down"
    
    def draw_to_surface(self, surface, frame_number):
        current_sprite = self.idle_animations[self.facing][
            frame_number % len(self.idle_animations[self.facing])
        ]
        surface.blit(current_sprite, self.position)
        
    def move(self, direction):
        self.facing = direction

        move_vector = {
            "up" : [0, -1],
            "down" : [0, 1],
            "left" : [-1, 0],
            "right" : [1, 0]
        }[direction]

        self.position[0] += move_vector[0] * TILE_SIZE
        self.position[1] += move_vector[1] * TILE_SIZE
        