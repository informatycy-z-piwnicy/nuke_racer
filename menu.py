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
from particles import Particle, Dust
pygame.init()


class Menu():
    def __init__(self, level, camera, previous_score):
        self.run = True
        self.exit_banner = False
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT), FULLSCREEN)
        self.bomb_current_surface = pygame.image.load('assets/menu/bomb.png').convert_alpha()
        self.player_surface = pygame.image.load('assets/player_model.png').convert_alpha()
        self.background = pygame.image.load('assets/background.png').convert_alpha()
        self.font = pygame.font.Font('assets/font.ttf', 70)
        self.level = level
        self.camera = camera
        self.previous_score_surface = self.font.render(str("Previous: " + str(previous_score)), True, (0,0,0))
        # start button
        self.start_button_surface = pygame.image.load('assets/menu/nuke.png').convert_alpha()
        self.start_button_pushed_surface = pygame.image.load('assets/menu/nuke_pushed.png').convert_alpha()
        self.start_button_current_surface = self.start_button_surface
        self.start_button_position = Vector2(WIDTH / 4, 440)
        self.start_button_rect = pygame.Rect(self.start_button_position.x, self.start_button_position.y, 960, 200)
        # exit button
        self.exit_button_surface = pygame.image.load('assets/menu/exit_button.png').convert_alpha()
        self.exit_button_pushed_surface = pygame.image.load('assets/menu/exit_button_pushed.png').convert_alpha()
        self.exit_button_current_surface = self.exit_button_surface
        self.exit_button_position = Vector2(WIDTH - 130, 0)
        self.exit_button_rect = pygame.Rect(self.exit_button_position.x, self.exit_button_position.y, 120, 120)
        # settings button
        self.settings_button_surface = pygame.image.load('assets/menu/settings_button.png').convert_alpha()
        self.settings_button_pushed_surface = pygame.image.load('assets/menu/settings_button_pushed.png').convert_alpha()
        self.settings_button_current_surface = self.settings_button_surface
        self.settings_button_position = Vector2(0, 0)
        self.settings_button_rect = pygame.Rect(self.settings_button_position.x, self.settings_button_position.y, 120, 120)

        # exit banner
        self.exit_banner_surface = pygame.image.load('assets/menu/exit_banner.png').convert_alpha()
        self.banner_button_surface = pygame.image.load('assets/menu/button.png').convert_alpha()
        self.banner_pushed_button_surface = pygame.image.load('assets/menu/pushed_button.png').convert_alpha()
        self.banner_exit_button_current_surface = self.banner_button_surface
        self.banner_exit_button_position = Vector2(WIDTH - WIDTH / 4 - 240, HEIGHT - HEIGHT / 4 - 130)
        self.banner_exit_button_rect = pygame.Rect(self.banner_exit_button_position.x, self.banner_exit_button_position.y, 120, 120)
        self.banner_resume_button_current_surface = self.banner_button_surface
        self.banner_resume_button_position = Vector2(WIDTH / 4 + 110, HEIGHT - HEIGHT / 4 - 130)
        self.banner_resume_button_rect = pygame.Rect(self.banner_resume_button_position.x, self.banner_resume_button_position.y, 120, 120)

        # bomb animation config
        self.dust = []
        self.color = (255,0,0)
        self.size = 100
        self.rad = 10

    # rendering menu
    def render(self):
        if self.run:
            self.screen.blit(self.background, (0, 0))
            self.level.render(self.screen, self.camera)
            self.screen.blit(self.player_surface, (WIDTH / 4, 840))
            self.screen.blit(self.bomb_current_surface, (-50, -10))
            self.screen.blit(self.start_button_current_surface, (WIDTH / 4, HEIGHT / 2 - 120))
            self.screen.blit(self.exit_button_current_surface, self.exit_button_position)
            self.screen.blit(self.settings_button_current_surface, self.settings_button_position)
            self.screen.blit(self.level.best_score_surface,(WIDTH / 2 - self.level.best_score_surface.get_width() / 2, 20))
            self.screen.blit(self.previous_score_surface,(WIDTH / 2 - self.previous_score_surface.get_width() / 2, 80))
            self.bomb_particles()
        if self.exit_banner:
            self.screen.blit(self.exit_banner_surface, (WIDTH / 4, HEIGHT / 4))
            self.screen.blit(self.banner_resume_button_current_surface, (self.banner_resume_button_position.x, self.banner_resume_button_position.y))
            self.screen.blit(self.banner_exit_button_current_surface, (self.banner_exit_button_position.x, self.banner_exit_button_position.y))
        pygame.display.update()

    # handling menu
    def loop(self):
        while self.run:
            # changing assets if under mouse
            mouse = pygame.mouse.get_pos()
            if self.start_button_rect.collidepoint(mouse):
                self.start_button_current_surface = self.start_button_pushed_surface
                if len(self.dust) == 0:
                    self.dust.append(Dust((self.start_button_current_surface.get_rect()[2]-580,self.start_button_current_surface.get_rect()[3]+330), self.rad, self.size, self.color, 10, "left", 1))
            elif self.exit_button_rect.collidepoint(mouse):
                self.exit_button_current_surface = self.exit_button_pushed_surface
            elif self.settings_button_rect.collidepoint(mouse):
                self.settings_button_current_surface = self.settings_button_pushed_surface
            else:
                if len(self.dust) > 0:
                    self.dust.pop(0)
                self.start_button_current_surface = self.start_button_surface
                self.exit_button_current_surface = self.exit_button_surface
                self.settings_button_current_surface = self.settings_button_surface
            # hendling events
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.run = False
                    pygame.quit()
                if event.type == MOUSEBUTTONDOWN:
                    if self.start_button_rect.collidepoint(mouse):
                        self.start()
                    elif self.exit_button_rect.collidepoint(mouse):
                        self.exit()
                    elif self.settings_button_rect.collidepoint(mouse):
                        self.settings()
            self.render()

    # when start button clicked
    def start(self):
        print('Start button clicked')
        self.run = False

    # when exit button clicked
    def exit(self):
        self.exit_banner = True
        while self.exit_banner:
            self.render()
            mouse = pygame.mouse.get_pos()
            if self.banner_resume_button_rect.collidepoint(mouse):
                self.banner_resume_button_current_surface = self.banner_pushed_button_surface
            elif self.banner_exit_button_rect.collidepoint(mouse):
                self.banner_exit_button_current_surface = self.banner_pushed_button_surface
            else:
                self.banner_exit_button_current_surface = self.banner_button_surface
                self.banner_resume_button_current_surface = self.banner_button_surface
            for event in pygame.event.get():
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    self.run = False
                    pygame.quit()
                if event.type == MOUSEBUTTONDOWN:
                    if self.banner_resume_button_rect.collidepoint(mouse):
                        self.exit_banner = False
                    elif self.banner_exit_button_rect.collidepoint(mouse):
                        pygame.quit()

    # when settings button clicked
    def settings(self):
        print('Settings button clicked')
        pygame.quit()

    # when cursor is on bomb
    def bomb_particles(self):
        for i in range(len(self.dust)):
            self.dust[i].draw(self.screen)
            self.dust[i].update_for_loop()
        if len(self.dust) > 1:
            self.dust.pop(0)

# launch only main menu
if __name__ == "__main__":
    camera = Camera()
    level = Level()
    menu = Menu(level, camera, 0) # previous score is 0 for tests only
    menu.loop()