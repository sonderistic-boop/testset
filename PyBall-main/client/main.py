import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))


import pygame as pg
from client.ui.menu import Menu

# design a pygame window, and set the window title as pyBall
pg.init()
pg.display.set_caption("pyBall")
screen = pg.display.set_mode((1600, 1000),pg.SRCALPHA)

# set up the clock
clock = pg.time.Clock()
# set up the main function for the game

def main():
    running = True
    focus = "Menu"
    menu = Menu(screen)
    while running:
        clock.tick(60)
        info = {
            "mouse" : pg.mouse.get_pos(),
            "events" : pg.event.get(),
            "focus" : focus
            }
        # set the maximum FPS
        
        
        # get all the events
        for event in info["events"]:
            # if the event is to quit the game, then set running as False
            if event.type == pg.QUIT:
                running = False
        
        menu.main(info)
        pg.display.flip()
            
        
        
        
        # if the focus is on the menu, then run the menu

main()

