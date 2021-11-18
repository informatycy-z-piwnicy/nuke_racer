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

    def follow_player(self, player):
        self.position.x += player.velocity.x

class Level():
    def __init__(self):
        self.ground_position = Vector2(0, 960)
        self.ground= [pygame.Rect(0, 960, 1920, BLOCK_SIZE)]
        self.ground_surface = pygame.image.load('assets/ground.png')
        self.font = pygame.font.SysFont("Arial",FONT_SIZE)

    # rendering and moving ground
    def render_ground(self, screen, camera):
        if self.ground_position.x <= -WIDTH:
            self.ground_position.x = 0
        else: self.ground_position.x -= 10
        screen.blit(self.ground_surface, (self.ground_position.x, 960))
        screen.blit(self.ground_surface, (self.ground_position.x + WIDTH, 960))

    # call other render functions
    def render(self, screen, camera, score):
        self.render_ground(screen, camera)
        self.reneder_score(screen,score)

    def reneder_score(self,screen,score):
    	score = str(score)
    	msg = "score: "+score
    	text = self.font.render(msg,True,(0,0,0))
    	screen.blit(text,(WIDTH-(50*len(msg)),0))

# launch new game on start
if __name__ == "__main__":
    new_game()