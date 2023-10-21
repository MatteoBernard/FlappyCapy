import pygame
from pygame import mask

from settings import *


class RocketCapy(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()

        self.game = game

        self.image = pygame.transform.scale(pygame.image.load("assets/rocketcapy.png").convert_alpha(), (100, 73))
        self.rect = self.image.get_rect()
        self.height = WINDOW_HEIGHT / 2
        self.rect.topleft = (WINDOW_WIDTH / 5, self.height)
        self.mask = mask.from_surface(self.image)

        self.jump_sound = pygame.mixer.Sound("assets/sounds/jump.mp3")
        self.jump_sound.set_volume(0.3)

    def update(self):
        self.place_capy()
        self.gravity()

    def place_capy(self):
        self.game.window.screen.blit(self.image, self.rect)
        self.rect.topleft = (self.rect.topleft[0], self.height)

    def jump(self):
        if self.height > 80:
            self.height -= 80
            self.jump_sound.play()

    def gravity(self):
        self.height += 1.4
