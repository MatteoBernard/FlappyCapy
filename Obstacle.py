import random
import pygame
from pygame import mask

from Window import Window

from settings import *


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, window: Window, img_path):
        super().__init__()

        self.image = pygame.image.load(img_path)
        pygame.transform.scale(self.image, (2, 2))
        self.rect = self.image.get_rect()
        self.window = window

        self.x = -1
        self.y = -1
        self.mask = None
        self.placerObstacleAleatoirement()

    def placerObstacleAleatoirement(self):
        self.x = WINDOW_WIDTH
        self.y = random.randint(0, WINDOW_HEIGHT - self.image.get_height())
        self.rect.topleft = (self.x, self.y)
        self.mask = mask.from_surface(self.image)

    def update(self):
        self.x -= 1
        self.rect.topleft = (self.x, self.y)
        self.window.screen.blit(self.image, (self.x, self.y))

    @staticmethod
    def generateRandomObstacle(game):
        path = random.choice(obstacle_images)
        obstacle = Obstacle(game.window, path)
        obstacle.x = WINDOW_WIDTH
        return obstacle
