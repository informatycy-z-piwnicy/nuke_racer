# endless runner, nuke themed game
# authors: D1N3SHh, Naris404, dzidek
# https://github.com/I-Z-P/nuke_racer


import random
import pygame
from pygame.math import Vector2
from config import *
from main import *


class Obstruction():
    def __init__(self):
        self.draw_variant()
        self.position = self.spawn()

    # draws variant
    def draw_variant(self):
        variant = random.randint(1, 3)
        if variant == 1:
            self.surface = pygame.image.load('assets/obstructions/one.png')
            self.rect = self.surface.get_rect()
        elif variant == 2:
            self.surface = pygame.image.load('assets/obstructions/two.png')
            self.rect = self.surface.get_rect()
        elif variant == 3:
            self.surface = pygame.image.load('assets/obstructions/three.png')
            self.rect = self.surface.get_rect()

    # draws position
    def spawn(self):
        return Vector2(random.randrange(WIDTH, WIDTH + 400), HEIGHT - 120 - self.rect.size[1])

    # scrolling obstructionect with map
    def move(self, shift):
        self.position.x -= shift.x

    # rendering single obstructionect
    def render(self, screen):
        screen.blit(self.surface, self.position)

    # check if obstructionect is still in use
    def in_use(self):
        if self.position.x + self.rect.size[0] > 0:
            return True
        else: return False


# spawning and handling obstructions
def handle_obstructions(obstruction, camera, screen):
    obstruction.move(camera.shift)
    obstruction.rect = pygame.Rect(obstruction.position.x, obstruction.position.y, obstruction.rect.size[0], obstruction.rect.size[1])
    obstruction.render(screen)
    if not obstruction.in_use():
        obstruction.draw_variant()
        obstruction.position = obstruction.spawn()


# launch new game on start
if __name__ == "__main__":
    new_game()