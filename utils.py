import pygame
from settings import *
import random 
# Function to start screen
def initialiseScreen():
    SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.flip()
    return SCREEN

def drawMycar(s,mycar):
    s.blit(MYCARPIX, (mycar.x, mycar.y) ) 


def drawOtherCars(s,cars):
    for car in cars :
        s.blit(ENNEMYPIX, (car.x, car.y) )
        
def moveEnnemies(cars):
    for car in cars :
        car.move()
# Class for a CAR

class Car:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 80 # width in px
        self.height = 59 # height in px
    
    
class myCar(Car):
    
    def __init__(self, x, y):
        super().__init__(x,y)
    
    def move(self,direction):
        if direction=="left" and self.x > self.width :
            self.x = self.x - self.width
        if direction == "right" and self.x < WIDTH - self.width :
            self.x = self.x + self.width
            
    
class ennemyCar(Car) :
    
    def __init__(self):
        super().__init__(0,0)
        posx = random.randint(35,WIDTH-35)
        posy = random.randint(-100,50)
        self.x= posx
        self.y = posy
        
    def move(self):
        self.y=self.y+5
        if self.y>HEIGHT :
            self.reset()
    
    def reset(self):
        posx = random.randint(35,WIDTH-35)
        posy = random.randint(-100,-self.height)
        self.x= posx
        self.y = posy
    
    