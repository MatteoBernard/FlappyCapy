import pygame
from pygame import mixer
from pygame.locals import USEREVENT

from RocketCapy import RocketCapy
from Obstacle import Obstacle
from Background import Background
from Window import Window

from settings import *
from json_manager import *


class Game:

    def __init__(self, window_size, background_path):

        pygame.init()
        pygame.time.set_timer(USEREVENT + 1, 4500)
        self.active = True

        self.background = Background(background_path, window_size)
        self.window = Window(window_size, self.background)
        self.rocket_capy = RocketCapy(self)
        self.clock = pygame.time.Clock()

        self.obstacles = set()  # Utilisation d'un ensemble pour stocker les obstacles

        self.score = 0
        self.font_size = 25
        self.font = pygame.font.Font("assets/CONSOLA.TTF", self.font_size)

        self.mixer = mixer
        self.mixer.init()
        self.mixer.music.load("assets/sounds/bg_music.mp3")
        self.mixer.music.set_volume(0.5)

    def collisions(self):
        for obstacle in self.obstacles:
            if pygame.sprite.collide_mask(self.rocket_capy, obstacle):
                self.active = False
        if self.rocket_capy.height >= WINDOW_HEIGHT - self.rocket_capy.mask.get_size()[1]:
            self.active = False

    def update_score(self):
        for obstacle in self.obstacles:
            if isinstance(obstacle, Obstacle):
                capy_center_x = self.rocket_capy.rect.centerx
                obstacle_center_x = obstacle.rect.centerx

                if capy_center_x == obstacle_center_x:
                    self.score += 1

    def display_score(self, score):
        score_text = self.font.render(str(score), True, (255, 255, 255))
        text_rect = score_text.get_rect()
        text_rect.center = (WINDOW_WIDTH // 2, 50)  # Centre horizontalement en utilisant WINDOW_WIDTH
        self.window.screen.blit(score_text, text_rect)

    def display_game_over_menu(self):

        # Mettre à jour le meilleur score avec le score actuel
        update_best_score(self.score)

        # Affiche le meilleur score
        meilleur_score_text = self.font.render(f"Meilleur score : {load_best_score()}", True, (255, 255, 255))
        meilleur_score_rect = meilleur_score_text.get_rect()
        meilleur_score_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 150)
        self.window.screen.blit(meilleur_score_text, meilleur_score_rect)

        text = self.font.render("Game Over", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
        self.window.screen.blit(text, text_rect)

        restart_text = self.font.render("Appuyez sur R pour rejouer", True, (255, 255, 255))
        restart_rect = restart_text.get_rect()
        restart_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 50)
        self.window.screen.blit(restart_text, restart_rect)

        quit_text = self.font.render("Appuyez sur Q pour quitter", True, (255, 255, 255))
        quit_rect = quit_text.get_rect()
        quit_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 100)
        self.window.screen.blit(quit_text, quit_rect)

        pygame.display.flip()

    def run(self):

        running = True
        self.mixer.music.play(-1)

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    self.active = False
                elif event.type == pygame.KEYDOWN and self.active:
                    if event.key == pygame.K_SPACE:
                        self.rocket_capy.jump()
                elif event.type == USEREVENT + 1 and self.active:
                    self.obstacles.add(Obstacle.generateRandomObstacle(self))

            if self.active:

                self.background.update()
                self.background.setup_background(self.window.screen)

                self.rocket_capy.update()

                obstacles_to_remove = set()

                for obstacle in self.obstacles:
                    obstacle.update()

                    if obstacle.rect.x < -500:
                        obstacles_to_remove.add(obstacle)  # Ajout des obstacles à supprimer

                # Suppression des obstacles en dehors de l'écran
                for obstacle in obstacles_to_remove:
                    self.obstacles.remove(obstacle)

                self.collisions()
                self.update_score()
                self.display_score(self.score)

                pygame.display.flip()
                self.clock.tick_busy_loop(FRAMERATE)

            else:
                self.display_game_over_menu()

                if not self.active:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_r]:
                        new = Game(self.window.size, self.background.img_path)
                        new.run()
                    if keys[pygame.K_q]:
                        running = False

    pygame.quit()
