# endless runner, nuke themed game
# authors: D1N3SHh, Naris404, dzidek
# https://github.com/I-Z-P/nuke_racer


import pygame
from pygame.constants import FULLSCREEN, MOUSEBUTTONDOWN
from pygame.math import Vector2
from level import *
from player import *
from config import *
from main import *
pygame.init()


class Menu():
    def __init__(self):
        self.run = True
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), FULLSCREEN)
        # start button
        self.start_button_surface = pygame.image.load('assets/menu/nuke.png')
        self.start_button_position = Vector2(WIDTH / 4, 440)
        self.start_button_rect = pygame.Rect(self.start_button_position.x, self.start_button_position.y, 960, 200)
        # exit button
        self.exit_button_surface = pygame.image.load('assets/menu/exit_button.png')
        self.exit_button_pushed_surface = pygame.image.load('assets/menu/exit_button_pushed.png')
        self.exit_button_current_surface = self.exit_button_surface
        self.exit_button_position = Vector2(WIDTH - 130, HEIGHT - 130)
        self.exit_button_rect = pygame.Rect(self.exit_button_position.x, self.exit_button_position.y, 120, 120)
        # settings button
        self.settings_button_surface = pygame.image.load('assets/menu/settings_button.png')
        self.settings_button_pushed_surface = pygame.image.load('assets/menu/settings_button_pushed.png')
        self.settings_button_current_surface = self.settings_button_surface
        self.settings_button_position = Vector2(WIDTH - 120, 0)
        self.settings_button_rect = pygame.Rect(self.settings_button_position.x, self.settings_button_position.y, 120, 120)
        # other
        self.bomb_surface = pygame.image.load('assets/menu/bomb.png')
        self.player_surface = pygame.image.load('assets/player_model.png')
        self.ground_surface = pygame.image.load('assets/ground.png')

    # rendering menu
    def render(self):
        self.screen.fill((49, 113, 181))

        self.screen.blit(self.player_surface, (WIDTH / 4, 840))             # make rendering from their class so they will move
        self.screen.blit(self.ground_surface, (0, 960))                     #

        if self.run:
            self.screen.blit(self.bomb_surface, (0, 0))
            self.screen.blit(self.start_button_surface, (WIDTH / 4 + 110, HEIGHT / 2 - 110))
            self.screen.blit(self.exit_button_current_surface, self.exit_button_position)
            self.screen.blit(self.settings_button_current_surface, self.settings_button_position)
        else:
            print('Now nuke animation is launching')

        pygame.display.update()

    # handling menu events
    def loop(self):
        while self.run:
            mouse = pygame.mouse.get_pos()
            if self.exit_button_rect.collidepoint(mouse):
                self.exit_button_current_surface = self.exit_button_pushed_surface
            elif self.settings_button_rect.collidepoint(mouse):
                self.settings_button_current_surface = self.settings_button_pushed_surface
            else:
                self.exit_button_current_surface = self.exit_button_surface
                self.settings_button_current_surface = self.settings_button_surface

            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.run = False
                    pygame.quit()
                if event.type == MOUSEBUTTONDOWN:
                    if self.start_button_rect.collidepoint(mouse):
                        self.run = False
                        self.render()
                        break
                    elif self.exit_button_rect.collidepoint(mouse):
                        self.exit()
                    elif self.settings_button_rect.collidepoint(mouse):
                        self.settings()
            self.render()

    # when exited button clicked
    def exit(self):
        print('Exit button clicked')
        pygame.quit()

    # when settings button clicked
    def settings(self):
        print('Settings button clicked')
        pygame.quit()


# launch only main menu
if __name__ == "__main__":
    menu = Menu()
    menu.loop()