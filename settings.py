import pygame



MODE = "AI" # or "AI"


# screen size : 
WIDTH = 600
HEIGHT = 600

# Frame rate while leanning
FRAME_RATE_AUTO = 500

# Frama rate while AI game
FRAME_RATE_AI = 10

MYCARPIX = pygame.image.load("./data/ship.png")
#sMYCARPIX = pygame.transform.scale(MYCARPIX,(50,50))

ENNEMYPIX = pygame.image.load("./data/ennemy.png")

MAX_ENNEMIES=10

#AI Settigns :
SAMPLES = 20000
FILENAME = "py_shooter_data.csv"
MODELNAME = "py_shooter.h5"