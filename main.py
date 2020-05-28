import sys
import pygame
from Game import *
from Start_menu import *

pygame.init()

width = 1080
height = 980

# on set la fenetre
pygame.display.set_caption("Sweet night declaration")
screen = pygame.display.set_mode((width, height))

game = Game()
start = Start_menu(game)
clock = pygame.time.Clock()

# image du background
background = pygame.image.load('assets/background.png').convert_alpha()

# boucle principale
while game.is_running:

    screen.blit(background, (0, 0))
    clock.tick(60)

    # boucle de jeu
    if game.is_playing:
        game.update(screen, start)
    # boucle du menu
    else:
        start.start_menu(screen)
    pygame.display.flip()
