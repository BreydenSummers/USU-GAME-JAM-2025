import pygame

class Game:
    def __init__(self, window_size = (400, 300), max_framerate = 30):
        self.window = pygame.display.set_mode((window_size))
        self.frame_timer = pygame.time.Clock()
        self.max_framerate = max_framerate

        self.running = True


    def window_size(self):
        return self.window.get_size()
    

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return 0
            print(event)

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
    game = Game()
    game.run_game()