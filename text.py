import pygame
import os

dir = os.getcwd()

class Text:
    def __init__(self):
        self.text = ""
    
    def show_Score():
        scoreFont = pygame.font.Font(f"{dir}\\{"textFonts"}\\KGHAPPY.ttf", 30)
        
        return scoreFont
    
    def HighScore(size):
        HighScoreFont = pygame.font.Font(f"{dir}\\{"textFonts"}\\Rows of Sunflowers.ttf", size)

        return HighScoreFont
    
    def timer(size):
        timerFont = pygame.font.Font(f"{dir}\\{"textFonts"}\\KGSoHighSchool.otf", size)

        return timerFont
    
    def loseHealth(size):
        loseHealthFont = pygame.font.Font(f"{dir}\\{"textFonts"}\\Fighting Spirit 2.otf", size)

        return loseHealthFont
    
    def textFont1(size, text, w, h, colour):
        textFont = pygame.font.Font(f"{dir}\\{"textFonts"}\\BaksoSapi.otf", size)
        TextSurface = textFont.render(f"{text}", False, colour)
        TextRect = TextSurface.get_rect(center=(w,h))
        return TextSurface, TextRect
