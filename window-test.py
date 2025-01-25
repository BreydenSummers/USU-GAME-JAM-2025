import pygame


SCREEN_SIZE = (400, 300)
MAX_FRAMERATE = 30

game_window = pygame.display.set_mode(SCREEN_SIZE)



def process_window_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        print(event)
    
    return True

def update_game_physics():
    pass

clock = pygame.time.Clock()
def update_window_graphics():
    game_window.fill((255, 255, 255))

    pygame.display.update()
    clock.tick(MAX_FRAMERATE)


def main_loop():
    running = True
    pygame.init()

    while running:
        running = process_window_events()

        update_game_physics()

        update_window_graphics()

    pygame.quit()

if __name__ == "__main__":
    main_loop()