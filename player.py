# endless runner, nuke themed game
# authors: D1N3SHh, Naris404, dzidek
# https://github.com/I-Z-P/nuke_racer


import pygame
from pygame.math import Vector2
from config import *
from main import *
import random


class Player():
    def __init__(self):
        self.position = Vector2(WIDTH / 4, 0)
        self.velocity = Vector2(10, 0)
        self.acceleration = Vector2(0.005, GRAVITY)
        self.model = pygame.image.load('assets/player_model.png')
        self.rect = self.model.get_rect()
        self.jump = False
        self.first_touch = True
        self.dust = []

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
                    self.dust.append(Dust(self.rect.midbottom))
                self.particle_splash(screen)
    # player movement
    def move(self,screen):
        if self.jump and self.on_ground:
            self.velocity.y -= 25
            self.acceleration.y = 1
            self.dust.append(Dust(self.rect.midbottom))
            self.first_touch = True
        self.particle_splash(screen)
        self.jump = False
        self.on_ground = False
        self.velocity += self.acceleration
        self.position += self.velocity
        self.position.x += ((WIDTH / 4) - self.position.x) # stick player to 1/4 of screen
        self.rect = pygame.Rect(self.position.x, self.position.y, BLOCK_SIZE, BLOCK_SIZE * 2)

    # rendering player
    def render(self, screen):
        screen.blit(self.model, self.rect)

    def particle_splash(self,screen):
        for i in range(len(self.dust)):
            if len(self.dust[i].particles) > 0:
                self.dust[i].draw(screen)
                self.dust[i].update()

class Particle:
    def __init__(self, pos):
        self.x, self.y = pos[0], pos[1]
        self.vx, self.vy = random.randint(-2, 2), random.randint(-10, 0)*.1
        self.rad = 10

    def draw(self, win):
        pygame.draw.circle(win, (170, 170, 170), (self.x, self.y), self.rad)
    
    def update(self):
        self.x += self.vx
        self.y += self.vy
        if random.randint(0, 100) < 40:
            self.rad -= 1

class Dust:
    def __init__(self, pos):
        self.pos = pos
        self.particles = []
        for i in range(100):
            self.particles.append(Particle(self.pos))

    def update(self):
        for i in self.particles:
            i.update()
            self.particles = [particle for particle in self.particles if particle.rad > 0]

    def draw(self, win):
        for i in self.particles:
            i.draw(win)

# launch new game on start
if __name__ == "__main__":
    new_game()