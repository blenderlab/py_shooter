import pygame
from settings import *
import random


def initialiseScreen():
    """Function to start screen"""
    SCREEN = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.flip()
    return SCREEN

def drawMycar(s,mycar):
    """ Putting player car on screen"""
    s.blit(MYCARPIX, (mycar.x, mycar.y) ) 


def drawOtherCars(s,cars):
    """ Drawing ennemies on screen """
    for car in cars :
        s.blit(ENNEMYPIX, (car.x, car.y) )
        
def moveEnnemies(cars):
    """ Apply move restults to each ennemy """
    for car in cars :
        car.move()


def countEnnemies(column,ennemies):
    """ Return the closest enemy distance, and the total in a column """ 
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
     """
        Main algorithm to chose the best move
        return the ACTION to perform & ennemies count left,front, rigth  
     """
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
    """ Appending game data to the DATA object
        0 - position of player (x only)
        1 - ennemy distance on the left column
        2 - ennemy distance on the center column
        3 - ennemy distance on the right column
    """
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
    """ saving DATA to a CSV file"""
    file =open(FILENAME,"w")
    for d in data:
        l = ""
        for c in d :
            l=l+str(c)
            l=l+","
        file.write(l+'\n')
    file.close()
            
    
def draw_vertical_lines(screen):
    """ TODO : draw lines/columns/counters to be more explicit  """
    pass

class Car:
    """ Generic CAR class """
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.width = 80 # width in px
        self.height = 59 # height in px
    
    
class myCar(Car):
    """ player class, inherit from CAR """
    def __init__(self, x, y):
        super().__init__(x,y)
    
    def move(self,direction):
        if direction=="left" and self.x > self.width :
            self.x = self.x - self.width
        if direction == "right" and self.x < (WIDTH - 2*self.width) :
            self.x = self.x + self.width
            
    
class ennemyCar(Car) :
    """ Ennemy car class, with some restriction in move"""
    
    
    def __init__(self):
        super().__init__(0,0)
        self.reset()
        
    def move(self):
        """ TODO : merge the move towards the parent class """
        self.y=self.y+59 #move by steps ...
        if self.y>HEIGHT :
            self.reset()
    
    def reset(self):
        """ respawn ennemy """
        nbRoads = (WIDTH//80)
        posx = random.randint(0,nbRoads-1)*80
        posy = -self.height * random.randint(1,30)
        self.x= posx
        self.y = posy
    
    