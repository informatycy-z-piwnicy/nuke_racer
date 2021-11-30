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
    player.start_time = time()
    clock = pygame.time.Clock()
    while run:
        clock.tick(TICKRATE)
        screen.blit(background, (0,0))
        player.check_score()
        handle_events(player)
        camera.follow_player(player)
        player.check_ground(level.ground,screen)
        player.move(screen)
        player.colisions(obstruction)
        level.render(screen, camera, player.score)
        player.render(screen)
        handle_obstructions(obstruction, camera, screen)
        if player.death:
            break
        pygame.display.update()
    new_game()


# init new game
def new_game():
    screen = pygame.display.set_mode((WIDTH, HEIGHT), FULLSCREEN)
    background = pygame.image.load('assets/background.png').convert_alpha()
    player = Player()
    camera = Camera()
    level = Level()
    obstruction = Obstruction()
    menu = Menu(level, camera)         # uncomment these lines to turn on main menu
    menu.loop()                        # or comment to turn off
    main_loop(True, screen, player, level, camera, obstruction, background)


# launch new game on start
if __name__ == "__main__":
    new_game()