# endless runner, nuke themed game
# authors: D1N3SHh, Naris404, dzidek
# https://github.com/I-Z-P/nuke_racer

import pygame
from pygame.math import Vector2
from config import *
from main import *

pygame.init()

class Camera():
    def __init__(self):
        self.position = Vector2(0, 0)
        self.shift = Vector2(5, 0)

    def follow_player(self, player):
        self.position.x += player.velocity.x
        self.shift = player.velocity

class Level():
    def __init__(self):
        self.ground_position = Vector2(0, 960)
        self.ground= [pygame.Rect(0, 960, 1920, BLOCK_SIZE)]
        self.ground_surface = pygame.image.load('assets/ground.png')
        self.font = pygame.font.SysFont("Arial",FONT_SIZE)
        # buildings for background
        self.building_one_surface = pygame.image.load('assets/buildings/building_one.png')
        self.building_one_rect = self.building_one_surface.get_rect()
        self.building_one_position = Vector2(100, HEIGHT - 130 - self.building_one_rect.size[1])
        self.building_two_surface = pygame.image.load('assets/buildings/building_two.png')
        self.building_two_rect = self.building_two_surface.get_rect()
        self.building_two_position = Vector2(400, HEIGHT - 130 - self.building_two_rect.size[1])
        self.building_three_surface = pygame.image.load('assets/buildings/building_three.png')
        self.building_three_rect = self.building_three_surface.get_rect()
        self.building_three_position = Vector2(800, HEIGHT - 130 - self.building_three_rect.size[1])
        self.building_four_surface = pygame.image.load('assets/buildings/building_four.png')
        self.building_four_rect = self.building_four_surface.get_rect()
        self.building_four_position = Vector2(1200, HEIGHT - 130 - self.building_four_rect.size[1])
        self.building_five_surface = pygame.image.load('assets/buildings/building_five.png')
        self.building_five_rect = self.building_five_surface.get_rect()
        self.building_five_position = Vector2(1600, HEIGHT - 130 - self.building_five_rect.size[1])

    # rendering paralax background
    def render_backgorund(self, screen, camera):
        # setting positions of buildings
        if self.building_one_position.x <= -self.building_one_rect.size[0]:
            self.building_one_position.x = WIDTH
        else: self.building_one_position.x -= camera.shift.x * 0.60
        if self.building_two_position.x <= -self.building_two_rect.size[0]:
            self.building_two_position.x = WIDTH
        else: self.building_two_position.x -= camera.shift.x * 0.58
        if self.building_three_position.x <= -self.building_three_rect.size[0]:
            self.building_three_position.x = WIDTH
        else: self.building_three_position.x -= camera.shift.x * 0.56
        if self.building_four_position.x <= -self.building_four_rect.size[0]:
            self.building_four_position.x = WIDTH
        else: self.building_four_position.x -= camera.shift.x * 0.54
        if self.building_five_position.x <= -self.building_five_rect.size[0]:
            self.building_five_position.x = WIDTH
        else: self.building_five_position.x -= camera.shift.x * 0.52
        # rendering
        screen.blit(self.building_one_surface, (self.building_one_position.x, self.building_one_position.y))
        screen.blit(self.building_two_surface, (self.building_two_position.x, self.building_two_position.y))
        screen.blit(self.building_three_surface, (self.building_three_position.x, self.building_three_position.y))
        screen.blit(self.building_four_surface, (self.building_four_position.x, self.building_four_position.y))
        screen.blit(self.building_five_surface, (self.building_five_position.x, self.building_five_position.y))

    # rendering and moving ground
    def render_ground(self, screen, camera):
        if self.ground_position.x <= -WIDTH:
            self.ground_position.x = 0
        else: self.ground_position.x -= camera.shift.x
        screen.blit(self.ground_surface, (self.ground_position.x, 950))
        screen.blit(self.ground_surface, (self.ground_position.x + WIDTH, 950))

    # call other render functions
    def render(self, screen, camera, score):
        self.render_backgorund(screen, camera)
        self.render_ground(screen, camera)
        self.reneder_score(screen, score)

    # rendering screen
    def reneder_score(self, screen, score):
        if score:
            score = str(score)
            msg = "score: "+score
            text = self.font.render(msg,True,(0,0,0))
            screen.blit(text,(WIDTH-(50*len(msg)),0))

# launch new game on start
if __name__ == "__main__":
    new_game()