import pygame


class Background(pygame.sprite.Sprite):

    def __init__(self, img_path, window_size):
        super().__init__()
        self.window_size = window_size
        self.img_path = img_path
        self.img = pygame.image.load(self.img_path)
        self.img = pygame.transform.scale(self.img, (self.img.get_width(), self.window_size[1]))
        self.rect = self.img.get_rect()
        self.x1 = 0
        self.x2 = self.rect.width  # Commencez la deuxième copie du fond à la largeur du fond

    def update(self):
        self.x1 -= 1
        self.x2 -= 1

        # Si la première copie du fond sort de l'écran
        if self.x1 < -self.rect.width:
            self.x1 = self.rect.width

        # Si la deuxième copie du fond sort de l'écran
        if self.x2 < -self.rect.width:
            self.x2 = self.rect.width

    def setup_background(self, screen):
        screen.blit(self.img, (self.x1, 0))
        screen.blit(self.img, (self.x2, 0))
