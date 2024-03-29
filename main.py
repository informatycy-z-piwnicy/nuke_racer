# endless runner, nuke themed game
# authors: D1N3SHh, Naris404, dzidek
# https://github.com/I-Z-P/nuke_racer


import pygame
from level import *
from player import *
from config import *
from menu import *
from obstructions import *


# keyboard handling
def handle_events(player):
    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            run = False
            pygame.quit()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE]:
            player.jump = True


# game loop
def main_loop(run, screen, player, level, camera, obstruction, background):
    level.start_time = time()
    clock = pygame.time.Clock()
    while run:
        clock.tick(TICKRATE)
        screen.blit(background, (0,0))
        handle_events(player)
        level.check_score()
        player.check_ground(level.ground)
        player.move()
        player.colisions(obstruction)
        camera.follow_player(player)
        level.render(screen, camera)
        player.render(screen)
        handle_obstructions(obstruction, camera, screen)
        if player.death:
            previous_score = level.previous_score
            break
        pygame.display.update()
    new_game(previous_score)


# init new game
def new_game(previous_score = 0):
    screen = pygame.display.set_mode((WIDTH, HEIGHT), FULLSCREEN)
    background = pygame.image.load('assets/background.png').convert_alpha()
    player = Player()
    camera = Camera()
    level = Level()
    obstruction = Obstruction()
    menu = Menu(level, camera, previous_score)         # uncomment these lines to turn on main menu
    menu.loop()                                        # or comment to turn off
    main_loop(True, screen, player, level, camera, obstruction, background)


# launch new game on start
if __name__ == "__main__":
    new_game()