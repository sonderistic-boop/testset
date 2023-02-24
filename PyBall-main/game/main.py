import pygame as pg
import math
#import twisted
#import numpy as np

import sys # for sys.exit()


from entities.pawn import Pawn
from entities.ball import Ball
from entities.stadium.line import Line
from entities.stadium.goal.goal import collidingGoal
import logic.physics as physics
from entities.stadium.arc import Arc
from entities.stadium.stadiums import smallStadium
from game import Game
pg.init() # initialises pg

#the colours used in the game

themeColours = {
    "red" : "#d14242",
    "green" : "#52d142",
    "blue" : "#426ad1",
    "yellow" : "#e1c16e",
    "cyan" : "#03b9b9",
    "magenta" : "#674ea7",
    "orange" : "#e69138"

}
#the maximum number of ticks per second
maxTicks = 60
screenBounds = (1600,1000)
screen = pg.display.set_mode(screenBounds,pg.SRCALPHA) # width, height
pg.display.set_caption("PyBall")


#need to set up a stadium class for future stadiums
field = pg.image.load("./shared/assets/tiles/fieldtiles/fieldtile.png")

#the clock object
clock = pg.time.Clock()

def runtime():
    #the main function
    running = True

    teamColoursguys = {"team1" : "red", "team2" : "blue"}
    guys = {"team1" : ["bigboyo"], "team2" : []}
    newgame = Game(screen,guys,300,3,"smallStadium",teamColoursguys)

    """
    newball = Ball(screen,(200,200),(30,30))
    newguy = Pawn("bigboyo","red",True,screen,(400,400),(70.3,70.3))
    
   
    newstadium = smallStadium(screen,(100,100),["red","blue"])
    guygroup =  (pg.sprite.GroupSingle(newguy))
    ballgroup = (pg.sprite.GroupSingle(newball))
    newarc = Arc(screen,(600,400),30,(0,math.pi/2),(255,255,255,128))
    """



    while running:
        #while running is true, the game will run
       
        clock.tick(maxTicks)

        for event in pg.event.get():
            #event handling loop
            match event.type:
                case pg.QUIT:
                    pg.quit()
                    sys.exit()


                
        keys = pg.key.get_pressed()
        newgame.leftTeam["bigboyo"].velocity[0] += (keys[pg.K_RIGHT] - keys[pg.K_LEFT]) * 0.1
        newgame.leftTeam["bigboyo"].velocity[1] += (keys[pg.K_DOWN] - keys[pg.K_UP]) * 0.1

        

        screen.fill((themeColours["green"]))
        newgame.run()
        
        pg.display.flip()
    
   
        if keys[pg.K_x]:
            physics.thrust(newgame.ball,newgame.leftTeam["bigboyo"])

        
    """
        screen.fill((themeColours["green"]))
    
        newguy.updatePhysics()
        newball.updatePhysics()

        newstadium.render()
        newball.render()
        newguy.render()
        newarc.render()
        #pg.draw.arc(screen,(themeColours["red"]),[500,200,400,400],0,math.pi,8)

        
        
        pg.display.flip()
    """




if __name__ == "__main__":
    runtime()
