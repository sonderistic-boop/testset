import pygame as pg

#set up a button class
class Button:
    def __init__(self,surface,pos,size,colour = (155,155,155,255),textColour = (255,255,255,255)):
        self.surface = surface
        self.position = pos
        self.size = size
        self.colour = colour
        self.borderColour = (0,0,0,255,255)
        self.text = ""
        self.textColour = textColour
        self.textSize = 20
        self.image = pg.Surface((self.size[0],self.size[1]),pg.SRCALPHA)
        self.rect = self.image.get_rect(topleft = (self.position[0],self.position[1]))
        

    def render(self):
        

        self.renderGraphics()

        
        
        if self.text != "":
            font = pg.font.SysFont("Arial",self.textSize)
            text = font.render(self.text,1,self.textColour)
            self.image.blit(text,(self.size[0]/2 - text.get_width()/2,self.size[1]/2 - text.get_height()/2))

        self.surface.blit(self.image,(self.position[0],self.position[1]))

    def renderGraphics(self):
        pg.draw.rect(self.image,self.colour,(0,0,self.size[0],self.size[1]))
        pg.draw.rect(self.image,self.borderColour,(0,0,self.size[0],self.size[1]),3)
        
        
    
    def eventHandler(self):
        pass
    def onClick(self):
        pass

    def onHover(self):
        pass

    def onLeave(self):
        pass

   
    def onTrigger(self):
        pass

    def onTriggerExit(self):
        pass

    def onTriggerStay(self):
        pass

    def onEnable(self):
        pass

    def onDisable(self):
        pass

   





class MenuButton(Button):
    def __init__(self,surface,pos,size,text,redirect):
        super().__init__(surface,pos,size,(51,102,0,255),(255,255,255,255))
        self.text = text
        self.colour = (51,102,0,255)
        self.borderColour = (76,153,0,255)
        self.redirect = redirect

        
    def eventHandler(self,info):
        if self.rect.collidepoint((info["mouse"])):
            for event in info["events"]:
                
                match event.type:
                    case pg.MOUSEBUTTONDOWN:
                        self.onClick()
     
        
    def onClick(self):
        print(self.redirect)
        return self.redirect
    
    def onHover(self):
        self.borderColour = (255,255,255,255)
    
    def onLeave(self):
        self.borderColour = (76,153,0,255)





    
    















class inputButton(Button):
    def __init__(self,surface,pos,size):
        super().__init__(surface,pos,size,(0,0,0,0))
        self.borderColour = (255,255,255)
        self.trigger = False
        
    def eventHandler(self,event,mouse):
            for event in event.type:

                match event:
                    case pg.MOUSEBUTTONDOWN:
                        #if mouse click and mouseposition in rect
                        if self.rect.collidepoint(mouse):
                            if self.trigger == False:
                                self.trigger = True
                        else:
                            if self.trigger:
                                self.trigger = False

                    case pg.KEYDOWN:
                        if self.trigger:
                            if event.key == pg.K_RETURN:
                                self.trigger = False
                            elif event.key == pg.K_BACKSPACE:
                                self.text = self.text[:-1]
                            else:
                                self.text += event.unicode
                    

