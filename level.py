# endless runner, nuke themed game
# authors: D1N3SHh, Naris404, dzidek
# https://github.com/I-Z-P/nuke_racer


import pygame
from pygame.math import Vector2
from config import *
from main import *
from time import sleep, time
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
        # assets section
        self.ground_position = Vector2(0, 960)
        self.ground= [pygame.Rect(0, 960, 1920, BLOCK_SIZE)]
        self.ground_surface = pygame.image.load('assets/ground.png').convert_alpha()
        self.font = pygame.font.Font('assets/font.ttf', 70)
        # buildings for background
        self.building_one_surface = pygame.image.load('assets/buildings/building_one.png').convert_alpha()
        self.building_one_rect = self.building_one_surface.get_rect()
        self.building_one_position = Vector2(100, HEIGHT - 130 - self.building_one_rect.size[1])
        self.building_two_surface = pygame.image.load('assets/buildings/building_two.png').convert_alpha()
        self.building_two_rect = self.building_two_surface.get_rect()
        self.building_two_position = Vector2(400, HEIGHT - 130 - self.building_two_rect.size[1])
        self.building_three_surface = pygame.image.load('assets/buildings/building_three.png').convert_alpha()
        self.building_three_rect = self.building_three_surface.get_rect()
        self.building_three_position = Vector2(800, HEIGHT - 130 - self.building_three_rect.size[1])
        self.building_four_surface = pygame.image.load('assets/buildings/building_four.png').convert_alpha()
        self.building_four_rect = self.building_four_surface.get_rect()
        self.building_four_position = Vector2(1200, HEIGHT - 130 - self.building_four_rect.size[1])
        self.building_five_surface = pygame.image.load('assets/buildings/building_five.png').convert_alpha()
        self.building_five_rect = self.building_five_surface.get_rect()
        self.building_five_position = Vector2(1600, HEIGHT - 130 - self.building_five_rect.size[1])
        # best score
        self.start_time = None
        self.score = None
        try:
            fd = open("best_score")
            self.best_score = int(fd.read())
            fd.close()
        except:
            self.best_score = 0
        self.best_score_surface = self.font.render(str("Best: " + str(self.best_score)), True, (0,0,0))

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
    def render(self, screen, camera):
        self.render_backgorund(screen, camera)
        self.render_ground(screen, camera)
        self.reneder_score(screen, self.score)

    # checking score and saving when best score is beaten
    def check_score(self):
        self.score = int(time() - self.start_time + 1)
        self.previous_score = self.score
        self.previous_score_surface = self.font.render(str("Previous: " + str(self.previous_score)), True, (0,0,0))
        if self.score > self.best_score:
            self.best_score = self.score
            self.best_score_surface = self.font.render(str("Best: " + str(self.best_score)), True, (0,0,0))
            fd = open("best_score","w")
            fd.write(str(self.best_score))
            fd.close()

    # rendering actual score
    def reneder_score(self, screen, score):
        if score:
            score = str(score)
            msg = "score: "+score
            text = self.font.render(msg,True,(0,0,0))
            screen.blit(text,(30, 30))

# launch new game on start
if __name__ == "__main__":
    new_game()