# endless runner, nuke themed game
# authors: D1N3SHh, Naris404, dzidek
# https://github.com/I-Z-P/nuke_racer


import pygame
from pygame.math import Vector2
from config import *
from main import *
import random
from particles import Particle, Dust
from time import sleep, time


class Player():
    def __init__(self):
        try:
            fd = open("best_score")
            self.best_score = int(fd.read())
            fd.close()
        except:
            self.best_score = 0
        self.start_time = None
        self.position = Vector2(WIDTH / 4, 0)
        self.velocity = Vector2(10, 0)
        self.acceleration = Vector2(0.002, GRAVITY)
        self.model = pygame.image.load('assets/player_model.png').convert_alpha()
        self.rect = self.model.get_rect()
        self.jump = False
        self.on_ground = False
        self.first_touch = True
        self.dust = []
        self.col = (170, 170, 170)
        self.dust_size = 100
        self.death = False
        # running animation
        self.current_running_surface = 0
        self.running_surfaces = []
        self.running_surfaces.append(pygame.transform.scale(pygame.image.load('assets/player/running_one.png').convert_alpha(), (60, 120)))
        self.running_surfaces.append(pygame.transform.scale(pygame.image.load('assets/player/running_two.png').convert_alpha(), (60, 120)))
        self.running_surfaces.append(pygame.transform.scale(pygame.image.load('assets/player/running_three.png').convert_alpha(), (60, 120)))
        self.running_surfaces.append(pygame.transform.scale(pygame.image.load('assets/player/running_four.png').convert_alpha(), (60, 120)))
        self.current_surface = self.running_surfaces[0]

    # checking if player is on ground and if so, it disables gravity
    def check_ground(self, ground, screen):
        self.acceleration.y = GRAVITY
        for tile in ground:
            if self.rect.colliderect(tile):
                self.position.y = tile.top - BLOCK_SIZE * 2 + 1
                self.acceleration.y *= 0
                self.velocity.y *= 0
                self.on_ground = True
                if self.first_touch == True:
                    self.first_touch = False
                    self.dust.append(Dust(self.rect.midbottom, 10, self.dust_size, self.col, self.velocity[0]/2))

    # player movement
    def move(self,screen):
        if self.on_ground: self.run_animation(0.2)
        if self.jump and self.on_ground:
            self.velocity.y -= 25
            self.acceleration.y = 1
            self.dust.append(Dust(self.rect.midbottom, 10, self.dust_size, self.col, self.velocity[0]/2))
            self.first_touch = True
        self.jump = False
        self.on_ground = False
        self.velocity += self.acceleration
        self.position += self.velocity
        self.position.x += ((WIDTH / 4) - self.position.x) # stick player to 1/4 of screen
        self.rect = pygame.Rect(self.position.x, self.position.y, BLOCK_SIZE, BLOCK_SIZE * 2)

    # rendering player
    def render(self, screen):
        screen.blit(self.current_surface, self.rect)
        self.particle_splash(screen)

    # runnig animation
    def run_animation(self, speed = 0.4):
        self.current_running_surface += speed
        if self.current_running_surface >= len(self.running_surfaces): self.current_running_surface = 0
        self.current_surface = self.running_surfaces[int(self.current_running_surface)]

    # creating partile slash while jumping and landing
    def particle_splash(self,screen):
        for i in range(len(self.dust)):
            if len(self.dust[i].particles) > 0:
                self.dust[i].draw(screen)
                self.dust[i].update()
        if len(self.dust) > 1:
            self.dust.pop(0)

    # checking score and saving when best score is beaten
    def check_score(self):
        self.score = int(time() - self.start_time + 1)
        if self.score > self.best_score:
            self.best_score = self.score
            fd = open("best_score","w")
            fd.write(str(self.best_score))
            fd.close()

    # checking if player colid with obstructions
    def colisions(self, obstruction):
        if self.rect.colliderect(obstruction.rect):
            self.death = True


# launch new game on start
if __name__ == "__main__":
    new_game()