import pygame


class Window:

    def __init__(self, window_size, background):
        pygame.display.set_caption("FlappyCapy")

        self.size = window_size
        self.screen = pygame.display.set_mode(self.size)
        self.background = background
