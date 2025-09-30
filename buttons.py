import pygame
import text
import interfaces
import main

w = interfaces.newScreen()[0]
h = interfaces.newScreen()[1]
screen = interfaces.newScreen()[2]
interface = interfaces.Interface(main.ScreenCode)

class Button:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def quitButton(self, x, y, mouse, colour1, colour2):
        ButtonText1 = text.Text.textFont1(20,"QUIT",x + self.w,self.h,(0,0,0))
        quitButtonTextSurface = ButtonText1[0]
        if x <= mouse[0] <= x+45 and y <= mouse[1] <= y+30:
            background = pygame.draw.rect(screen,colour2,[x,y, x + self.w, y + self.h])
            button1 = screen.blit(quitButtonTextSurface,background)
        else:
            background = pygame.draw.rect(screen,colour1,[x,y, x + self.w, y + self.h])
            button1 = screen.blit(quitButtonTextSurface,background)
        
        return button1
    
    def exitGame(self, x, y, mouse, colour1, colour2):
        button1Frame = ((x/2 - 200,y-110),(self.w + 310,self.h+ 60))
        ButtonText1 = text.Text.textFont1(55,"Close Game",x/2,y-110,(0,0,0))
        closeButtonTextSurface = ButtonText1[0]
        if x/2-200 <= mouse.get_pos()[0] <= 830 and y-110 <= mouse.get_pos()[1] <= 655:
            #print("hello")
            background = pygame.draw.rect(screen,colour2,button1Frame)
            button1 = screen.blit(closeButtonTextSurface,background)
        else:
            background = pygame.draw.rect(screen,colour1,button1Frame)
            button1 = screen.blit(closeButtonTextSurface,background)
        
        return button1
    
    def playSinglePlayer(self, x, y, mouse, colour1, colour2):
        button1Frame = ((x/2 - 200,y-210),(self.w + 310,self.h+ 60))
        ButtonText1 = text.Text.textFont1(47,"SinglePlayer",x/2,y-110,(0,0,0))
        closeButtonTextSurface = ButtonText1[0]
        if x/2-200 <= mouse.get_pos()[0] <= 830 and y-210 <= mouse.get_pos()[1] <= 555:
            #print("hello")
            background = pygame.draw.rect(screen,colour2,button1Frame)
            button1 = screen.blit(closeButtonTextSurface,background)
        else:
            background = pygame.draw.rect(screen,colour1,button1Frame)
            button1 = screen.blit(closeButtonTextSurface,background)
        
        return button1
    
    def stats(self, x, y, mouse, colour1, colour2):
        button1Frame = ((x - 135,5),(self.w + 110,self.h+ 50))
        ButtonText1 = text.Text.textFont1(45,"Stats",x/2,y-110,(0,0,0))
        closeButtonTextSurface = ButtonText1[0]
        if x - 135 <= mouse.get_pos()[0] <= 1395 and 5 <= mouse.get_pos()[1] <= 60:
            #print("hello")
            background = pygame.draw.rect(screen,colour2,button1Frame)
            button1 = screen.blit(closeButtonTextSurface,background)
        else:
            background = pygame.draw.rect(screen,colour1,button1Frame)
            button1 = screen.blit(closeButtonTextSurface,background)
        
        return button1
    
    def Back(self, x, y, mouse, colour1, colour2):
        button1Frame = ((x - 135,y - 60),(self.w + 110,self.h+ 50))
        ButtonText1 = text.Text.textFont1(47,"Back",x/2,y-110,(0,0,0))
        closeButtonTextSurface = ButtonText1[0]
        if x - 135 <= mouse.get_pos()[0] <= 1395 and y-60 <= mouse.get_pos()[1] <= 695:
            #print("hello")
            background = pygame.draw.rect(screen,colour2,button1Frame)
            button1 = screen.blit(closeButtonTextSurface,background)
        else:
            background = pygame.draw.rect(screen,colour1,button1Frame)
            button1 = screen.blit(closeButtonTextSurface,background)
        
        return button1
    
    def playMultiplayer(self, x, y, mouse, colour1, colour2):
        button1Frame = ((x/2 - 200,y-310),(self.w + 310,self.h+ 60))
        ButtonText1 = text.Text.textFont1(47,"Multiplayer",x/2,y-110,(0,0,0))
        closeButtonTextSurface = ButtonText1[0]
        if x/2-200 <= mouse.get_pos()[0] <= 830 and y-310 <= mouse.get_pos()[1] <= 455:
            #print("hello")
            background = pygame.draw.rect(screen,colour2,button1Frame)
            button1 = screen.blit(closeButtonTextSurface,background)
        else:
            background = pygame.draw.rect(screen,colour1,button1Frame)
            button1 = screen.blit(closeButtonTextSurface,background)
        
        return button1
        

