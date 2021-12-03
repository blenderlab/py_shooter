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

def countEnnemies(column,ennemies):
    tot_ennemies = 0
    closest = 0
    colx= column 
    for ennemy in ennemies :
        if ennemy.y>0:
            if (ennemy.x == colx):
                tot_ennemies = tot_ennemies +1
                if (ennemy.y > closest) :
                    closest = ennemy.y
    return(closest,tot_ennemies) 
    
def chooseNextMove(mycar,ennemies):
     # trying a random move :
     #actions =  ["left","right","stay"]
     #action = random.choice(actions)
     # count ennemies around : 
     left_closest, left_tot = countEnnemies(mycar.x-80,ennemies)
     right_closest, right_tot = countEnnemies(mycar.x+80,ennemies)
     stay_closest, stay_tot = countEnnemies(mycar.x,ennemies)
     allDistances=[left_closest,stay_closest,right_closest]
     
     if (stay_closest==0):
         return ("stay",allDistances)
     print(mycar.x,WIDTH-80)
     if (mycar.x == 480):
         if (stay_closest>left_closest):
             return("left",allDistances)
         else :
             return ("stay",allDistances)
             
             
     if (mycar.x == 0):
         if (stay_closest>right_closest):
             return ("right",allDistances)
         else :
             return ("stay",allDistances)
         
     if (stay_closest>right_closest):
         return ("right",allDistances)

     else :
         if (right_closest>left_closest):
             return ("left",allDistances)
         else :
             return ("stay",allDistances)
         
def saveData(data,action, mycar,alldistances):
    if action=="left" : idx = 1
    if action=="stay" : idx = 2
    if action=="right" : idx = 3
    row = []
    row.append(mycar.x)
    row.append(alldistances[0])
    row.append(alldistances[1])
    row.append(alldistances[2])
    row.append(idx)
    data.append(row)

def writedata(data):
    file =open("py_shooter_data.csv","w")
    for d in data:
        str = ""
        for c in d :
            str.append(c)
            str.append(",")
        file.write(d)
    file.close()
            
    
def draw_vertical_lines(screen):
    pass

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
        if direction == "right" and self.x < (WIDTH - 2*self.width) :
            self.x = self.x + self.width
            
    
class ennemyCar(Car) :
    
    def __init__(self):
        super().__init__(0,0)
        self.reset()
        
    def move(self):
        self.y=self.y+59 #move by steps ...
        if self.y>HEIGHT :
            self.reset()
    
    def reset(self):
        nbRoads = (WIDTH//80)
        posx = random.randint(0,nbRoads-1)*80
        posy = -self.height * random.randint(1,30)
        self.x= posx
        self.y = posy
    
    