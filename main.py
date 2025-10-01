import pygame
import interfaces

pygame.init()

# Ensure there is a display. If interfaces sets it, you can remove this line.
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

ScreenCode = 0
Interface = interfaces.Interface(ScreenCode)

def MainMenu():
    return Interface.mainMenu()

def Stats():
    return Interface.stats()

def SinglePlayer():
    return Interface.singlePlayer()

def MultiPlayer():
    return Interface.multiplayer()

if __name__ == '__main__':
    run = True
    while run:
        # 1) Process events every frame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # 2) Route to the active screen ONCE and use its return
        if ScreenCode == 0:
            ScreenCode = MainMenu()
        elif ScreenCode == 1:
            ScreenCode = SinglePlayer()
        elif ScreenCode == 2:
            ScreenCode = Stats()
        elif ScreenCode == 3:
            ScreenCode = MultiPlayer()
        else:
            ScreenCode = 0  # fallback

        # 3) Update the display and cap FPS
        pygame.display.flip()   # or pygame.display.update()
        clock.tick(60)

    pygame.quit()
