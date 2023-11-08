import pygame as pg
import random
from sys import path
from sys import exit
import os
import Text

my_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(my_path)
path.append(my_path)

#Colours
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)

#Setup
pg.init()
#set your window size, (x,y)
screen = pg.display.set_mode((800,600))
pg.display.set_caption("Game Title")
clock = pg.time.Clock()
thing = pg.image.load("target.png")
randx = random.randint(0,725)
randy = random.randint(75,525)
score = 0
time = 0
mode = 0

class target ():
    #class variables
    W = 30
    H = 30
    thing = pg.image.load("target.png")

    def __init__ (self, iny, incolour):
        #Attributes
        self.hitbox = pg.Rect(randx, randy, 75, 75)
        self.colour = incolour
    def update(self):
        randx = random.randint(0,725)
        randy = random.randint(75, 525)
        self.hitbox[0] = randx
        self.hitbox[1] = randy
    def draw(self):
        pg.draw.ellipse(screen, self.colour, self.hitbox)
        screen.blit(thing,(self.hitbox[0], self.hitbox[1]))

aim = target(randy, red)

while True:

    while mode == 0:

        pg.event.pump()
        #1. UPDATES
        #Move objects to new locations based on speed



        #2. INPUTS
        #Check all input devices (Ex: Keyboard / Mouse)

        keys = pg.key.get_pressed()
        mx, my = pg.mouse.get_pos()
        L,M,R = pg.mouse.get_pressed()


        #3. EVENTS
        #Set of if-statements for different events of interest (Ex. Objects colliding, moving off screen etc.)

        time = time + 0.1

        if mx > aim.hitbox[0]  and mx < aim.hitbox[0] + 75 and my > aim.hitbox[1]  and my < aim.hitbox[1] + 75 and L ==1:
            screen.fill(black)
            aim.update()
            score = score+1

        if time >= 25:
            mode = 1

        #4. DRAWING
        #Draw the current state of everything in the game (frame)

        aim.draw()
        pg.display.flip()
        Text.printText(screen, white, score , 10,10, 50)

        #5. CLOCK
        #Set how many frame per second the game will run at
        clock.tick(30)

    while mode == 1:

        pg.event.pump()
        #1. UPDATES
        #Move objects to new locations based on speed


        #2. INPUTS
        #Check all input devices (Ex: Keyboard / Mouse)

        keys = pg.key.get_pressed()
        mx, my = pg.mouse.get_pos()
        L,M,R = pg.mouse.get_pressed()


        #3. EVENTS
        #Set of if-statements for different events of interest (Ex. Objects colliding, moving off screen etc.)

        if keys[pg.K_SPACE] == True:
            mode = 0
            time = 0
            score = 0

        #4. DRAWING
        #Draw the current state of everything in the game (frame)

        avscore = score/25

        screen.fill(black)
        Text.printText(screen, white, 'Score:' , 100,200, 50)
        Text.printText(screen, white, score , 230,200, 50)
        Text.printText(screen, white, 'Targets Hit Per Second:', 100,300, 50)
        Text.printText(screen, white, avscore , 520,300, 50)
        Text.printText(screen, white, 'Press Space To Try Again' , 100,500, 50)
        pg.display.flip()

        #5. CLOCK
        #Set how many frame per second the game will run at
        clock.tick(30)
