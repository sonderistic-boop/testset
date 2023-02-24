import os, sys
from os.path import dirname, join, abspath
sys.path.insert(0, abspath(join(dirname(__file__), '..')))


import pygame

from server.network import Network
import pickle
#pygame.font.init()

width = 700
height = 700
#win = pygame.display.set_mode((width, height))
#pygame.display.set_caption("pyBall-Client")






class Client:
    def __init__(self,serverIp):
        self.serverIp = input("Enter server IP: ")
        self.networkInterface = Network(self.serverIp)
        print(self.networkInterface.getInitData())

    
    
    def preGameUpdate(self):
        print("nice")
      

    def clientMain(self):
        run = True
        clock = pygame.time.Clock()

        print("You are player")

        while run:
            clock.tick(60)
            try:
                game = self.networkInterface.send("get")
            except Exception as wow:
                print(wow)
                run = False
                print("Couldn't get game")
                break

newclient = Client("localhost")
while True:
    newclient.clientMain()