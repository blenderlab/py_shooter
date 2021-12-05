import pygame
from  settings import * 
from  utils import *
import random 

pygame.init()
pygame.display.set_caption("Racing with an AI")

SCREEN = initialiseScreen()

# define the clock :
clock = pygame.time.Clock()

# let's create our brand new car !
my_car = myCar(80*3, HEIGHT*0.8)

# let's add some bad boyz :
ennemies = [] # array of ennemies
for _ in range(MAX_ENNEMIES):
    ennemies.append(ennemyCar())
data=[]
sampleCounter=0
while 1 :
    # manage the speed :
    clock.tick(FRAME_RATE)
    # force all events to be processed : 
    pygame.event.pump()
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_LEFT:
                my_car.move('left')
            if event.key == pygame.K_RIGHT:
                my_car.move('right')
            if event.key == pygame.K_ESCAPE:
                pygame.quit() # close pygame
                raise SystemExit #for a system close  
    
    # Autopilot (sort of...) 
    nextAction,alldistances = chooseNextMove(my_car,ennemies)    
    saveData(data,nextAction, my_car,alldistances)
    
    my_car.move(nextAction)
    
    # check counter before saving data : 
    if sampleCounter == SAMPLES:
        writedata(data)
    else :
        sampleCounter=sampleCounter+1
        print("Sample  ",sampleCounter, "/", SAMPLES) 
    
    # fill the screen with black : 
    SCREEN.fill(0)
    
    # update screen :
    moveEnnemies(ennemies)
    drawMycar(SCREEN, my_car) # display my own ship
    drawOtherCars(SCREEN, ennemies) # and others tooo....
    pygame.display.flip()