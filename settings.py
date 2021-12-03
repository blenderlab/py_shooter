import pygame

FRAME_RATE = 30

# screen size : 
WIDTH = 600
HEIGHT = 600


MYCARPIX = pygame.transform.scale((pygame.image.load("./data/ship.png")),(50,50))
MYCARPIX = pygame.transform.scale(MYCARPIX,(50,50))


ENNEMYPIX = pygame.image.load("./data/ennemy.png")

MAX_ENNEMIES=10