import pygame

FRAME_RATE = 500

# screen size : 
WIDTH = 600
HEIGHT = 600


MYCARPIX = pygame.image.load("./data/ship.png")
#sMYCARPIX = pygame.transform.scale(MYCARPIX,(50,50))


ENNEMYPIX = pygame.image.load("./data/ennemy.png")

MAX_ENNEMIES=10

#AI Settigns :
SAMPLES = 20000
