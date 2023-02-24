#make game class, with a run method, and a main method
#game should be 810x770
#game will have a stadium, a ball, and two teams
#game will have a run method, which will run the game
#game 
import pygame as pg
import math
import sys


import logic.physics as physics
import logic.collisions as col
from entities.pawn import Pawn
from entities.ball import Ball
import entities.stadium.stadiums as stadiums


class Game():
    def __init__(self,parentScreen,players,time,maxScore,stadium,colours):
        self.size = (1920,1080)
        #declares the parent screen, which is the screen that the game surface will be drawn on
        self.parentScreen = parentScreen
        #declares which stadium the game will be played on
        self.stadium = stadium

        #declares how long the game will last
        self.time = time
        #declares the maximum score the game will be played to
        self.maxScore = maxScore

        self.teamColours = colours

        self.leftTeam = {}
        self.rightTeam = {}

        self.leftTeamScore = 0
        self.rightTeamScore = 0

        
        
        
        #load game surface, load players, load ball, load stadium
        

        self.screen = pg.Surface((self.size),pg.SRCALPHA)
        
        self.stadium = getattr(stadiums,stadium)
        self.stadium = self.stadium(self.screen,(100,100),[colours["team1"],colours["team2"]])
        
        
        self.ball = Ball(self.screen,(self.stadium.bounds["middle"][0],self.stadium.bounds["middle"][1]),(30,30))
        
        #load players, and add them to the left and right team dictionaries. initial position will be the middle-left of the stadium for the left team, and the middle-right of the stadium for the right team
        for i in players["team1"]:
            self.leftTeam[i] = Pawn(i,colours["team1"],False,self.screen,(400,400),(70.3,70.3))          
        
        for i in players["team2"]:
            self.rightTeam[i] = Pawn(i,colours["team2"],False,self.screen,(400,400),(70.3,70.3))   

        
        
        
        #add sprite groups for ball, players, stadium parts

        #self.ballGroup = pg.sprite.GroupSingle(self.ball)


        self.playerGroup = pg.sprite.Group()
        self.playerGroup.add(self.leftTeam.values())
        self.playerGroup.add(self.rightTeam.values())


        self.stadiumBoundsGroup = pg.sprite.Group()
        self.stadiumBoundsGroup.add(self.stadium.lines.values())
        self.stadiumBoundsGroup.add(self.stadium.collidingGoals.values())

        self.stadiumGoalGroup = pg.sprite.Group()
        self.stadiumGoalGroup.add(self.stadium.goals.values())



    def run(self):
        #check for collisions, check for goals, check for time, check for score
        #update the ball, update the players
        #render the stadium, render the ball, render the players
        self.collisionChecker()
        self.updatePhysics()
        self.render()
        
           


    def render(self):
        #draw the stadium, draw the ball, draw the players
        self.stadium.render()
        for i in self.playerGroup:
            i.render()
        self.ball.render()
        
        
        self.parentScreen.blit(self.screen,(0,50))

    def updatePhysics(self):
        #update the ball, update the players
        self.ball.updatePhysics()
        for i in self.playerGroup:
            i.updatePhysics()
        
    
    def collisionChecker(self):
        #check for collisions between the ball and the players, and the ball and the stadium
        #check for collisions between the players and the stadium
        #check for collisions between the players and the other players
        #check for collisions between the ball and the goals
        #check for collisions between the players and the goals
        

        #check for collisions between the ball and the players
        ballPlayerCollisions = pg.sprite.spritecollide(self.ball,self.playerGroup,False,pg.sprite.collide_mask)

        ballStadiumCollisions = pg.sprite.spritecollide(self.ball,self.stadiumBoundsGroup,False,pg.sprite.collide_mask)

        ballGoalCollisions = pg.sprite.spritecollide(self.ball,self.stadiumGoalGroup,False,pg.sprite.collide_mask)

        playerStadiumCollisions = pg.sprite.groupcollide(self.playerGroup,self.stadiumBoundsGroup,False,pg.sprite.collide_mask)

        playerPlayerCollisions = pg.sprite.groupcollide(self.playerGroup,self.playerGroup,False,False,pg.sprite.collide_mask)


        for i in ballGoalCollisions:
            self.goalScored(i)


        for i in ballStadiumCollisions:
            if i.collidesWith["ball"]:
                print("hit")
                physics.objectCollision(i,self.ball,col.circleQuadManifold(i,self.ball))

        for i in ballPlayerCollisions:
            physics.objectCollision(self.ball,i)

        
    """  
        for i in playerStadiumCollisions:
            for j in playerStadiumCollisions[i]:
                physics.objectCollision(i,j)
        
        for i in playerPlayerCollisions:
            for j in playerPlayerCollisions[i]:
                physics.objectCollision(i,j)
        """
        
        
        #for i in ballStadiumCollisions:
        
    def goalScored(self,goal):
        
        if goal.team == self.teamColours["team1"]:
            self.rightTeamScore += 1
        elif goal.team == self.teamColours["team2"]:
            self.leftTeamScore += 1

        
        self.reset()



    def reset(self):
        self.ball.reset()
        for i in self.playerGroup:
            i.reset()
    

    




        
        

        
    