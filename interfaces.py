import pygame
import text
from Player import player
import random as rand
import os
import items
from network import Network

def newScreen():
    w = 1400
    h = 700
    screen = pygame.display.set_mode((w,h))

    return w, h, screen

pygame.init()
pygame.display.set_caption("Game #1")

# GLOBAL VARIABLES
dir = os.getcwd()
w = newScreen()[0]
h = newScreen()[1]
screen = newScreen()[2]
clock = pygame.time.Clock()

class Interface:
    def __init__(self, ScreenCode):
        self.ScreenCode = ScreenCode
        self.mouse = pygame.mouse

# MAIN MENU
    def mainMenu(self):
        import buttons

        def Generate_Item(item, getItem, X, Y):
                    itemFrame = item.spawn(X,Y) # Spawns item on random x and y positions
                    screen.blit(getItem,itemFrame) # Displays item

                    return itemFrame
        
        def main():
            run = True
            ScreenCode = self.ScreenCode
            Button = buttons.Button(20,5)

            itemList = ["bomb.png","coin.png","idle.png","player.png","playerR.png","runMan.png","runMan2.png","ExplosionBomb.png","SizeDown.png","sonic.png"]
            move = -100
            random = rand.choice(itemList)
            item = items.Items(200,200,random)
            getItem = item.get_Item()
            while run:
                mouse = self.mouse
                mouse.set_cursor(0)
                #print(mouse.get_pos())
                screen.fill((23,50,0))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if w/2-200 <= mouse.get_pos()[0] <= 830 and h-110 <= mouse.get_pos()[1] <= 655:
                            pygame.quit()
                            exit()
                        if w/2-200 <= mouse.get_pos()[0] <= 830 and h-210 <= mouse.get_pos()[1] <= 555:
                            #print(ScreenCode)
                            ScreenCode = 1
                            #print(ScreenCode)
                            return ScreenCode
                        if w - 135 <= mouse.get_pos()[0] <= 1395 and 5 <= mouse.get_pos()[1] <= 60:
                            mouse.set_cursor(11)
                            ScreenCode = 2
                            return ScreenCode
                        if w/2-200 <= mouse.get_pos()[0] <= 830 and h-310 <= mouse.get_pos()[1] <= 455:
                            mouse.set_cursor(11)
                            ScreenCode = 3
                            return ScreenCode
                    
                itemGenerate = Generate_Item(item, getItem, move, 250)
                if itemGenerate.left < w:
                    move += 3
                    itemGenerate.x += move
                else:
                    random = rand.choice(itemList)
                    item = items.Items(200,200,random)
                    getItem = item.get_Item()
                    move = -100
                
                Button.playMultiplayer(w,h,mouse,(100,100,100), (170,170,170))[0]
                Button.exitGame(w,h,mouse,(100,100,100), (170,170,170))[0]
                Button.playSinglePlayer(w,h,mouse,(100,100,100), (170,170,170))[0]
                Button.stats(w,h,mouse,(100,100,100), (170,170,170))[0]
                pygame.display.update()
                clock.tick(60)
        return main()

    # PLAYER STATS
    def stats(self):
        import buttons

        HighScoreText = text.Text.HighScore(50)
        BestSizeText = text.Text.HighScore(50)

        def highScoreText(highScore):
            highScoreSurface = HighScoreText.render(f"Personal Best: {highScore}", False, (0))
            highScoreRect = highScoreSurface.get_rect(center=(w/2,h/2-200))

            return highScoreSurface, highScoreRect
        
        def bestSizeText(bestSize):
            bestSizeSurface = BestSizeText.render(f"Largest Size: {bestSize}", False, (0))
            bestSizeRect = bestSizeSurface.get_rect(center=(w/2,h/2-100))

            return bestSizeSurface, bestSizeRect

        try:
            with open(f'{dir}\\Extra\\spHighScore') as file:
                personalHighScore = int(file.read())
        except FileNotFoundError:
            print("File not found")
        
        try:
            with open(f'{dir}\\Extra\\spLargestSize') as file:
                personalBestSize = int(file.read())
        except FileNotFoundError:
            print("File not found")

        def main():
            run = True
            ScreenCode = self.ScreenCode
            Button = buttons.Button(20,5)
            
            while run:
                mouse = self.mouse
                #print(mouse.get_pos())
                mouse.set_cursor(0)
                screen.fill((23,50,0))

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if w - 135 <= mouse.get_pos()[0] <= 1395 and h-60 <= mouse.get_pos()[1] <= 695:
                            ScreenCode = 0
                            return ScreenCode

                Button.Back(w,h,mouse,(100,100,100), (170,170,170))[0]
                screen.blit(highScoreText(personalHighScore)[0],highScoreText(personalHighScore)[1])
                screen.blit(bestSizeText(personalBestSize)[0],bestSizeText(personalBestSize)[1])
                pygame.display.update()
                clock.tick(60)
        return main()


    def multiplayer(self):
        import buttons

        def main():

            run = True
            speed = 2
            ScreenCode = self.ScreenCode
            Button = buttons.Button(20,5)
            n = Network()
            p1 = n.getP()
            print(p1)
            print(type(p1))

            tick_time_start = 1

            def redrawWindow(screen, player1Frame, player2Frame):
                screen.fill((48,69,41))
                
                keys = pygame.key.get_pressed()

                if keys[pygame.K_w]:
                        player1Frame.y -= speed # Moves PlayerBox Up
                        player1Frame = p1.Spawn_Player(player1Character, player1Frame.x, player1Frame.y)
                        

                if keys[pygame.K_s]:
                        player1Frame.y += speed # Moves PlayerBox Down
                        player1Frame = p1.Spawn_Player(player1Character, player1Frame.x, player1Frame.y)
                        

                if keys[pygame.K_a]:
                        player1Frame.x -= speed # Moves PlayerBox left
                        player1Frame = p1.Spawn_Player(player1Character, player1Frame.x, player1Frame.y) # Spawns in new player at same x and y position

                if keys[pygame.K_d]:
                        player1Frame.x += speed # Moves PlayerBox Right
                        player1Frame = p1.Spawn_Player(player1Character, player1Frame.x, player1Frame.y)
                        

                screen.blit(player1Character,player1Frame)
                screen.blit(player2Character,player2Frame)
                pygame.display.update()

            try:
                while run:
                    tick_time_start += 1
                    mouse = self.mouse
                    clock.tick(60)
                    p2 = n.send(p1)

                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_LSHIFT:
                                speed = speed * 2
                        elif event.type == pygame.KEYUP:
                            if event.key == pygame.K_LSHIFT:
                                if speed > 2:
                                    speed = speed / 2

                    if tick_time_start > 1 and tick_time_start < 50:
                        player1Character = p1.get_character()[1]
                        player2Character = p2.get_character()[1]
                        print(p1)
                        player1Frame = p1.Spawn_Player(player1Character,(w/2)-50,h/2)
                        player2Frame = p2.Spawn_Player(player2Character,(w/2)+50,h/2)

                    redrawWindow(screen, player1Frame, player2Frame)

            except AttributeError as a:
                print(f"Error: Problem with Server")
                print(a)
                pygame.quit()
                exit()
        return main()

# SINGLE PLAYER
    def singlePlayer(self):
        import buttons
        game = True
        cw = 80
        ch = 80
        ScoreText = text.Text.show_Score()
        HighScoreText = text.Text.HighScore(30)
        reduceHealthText = text.Text.loseHealth(30)
        CurrentSizeText = text.Text.HighScore(30)
        speed = 2

        def scoreText(score):
            scoreSurface = ScoreText.render(f"Score: {score}", False, (0))
            scoreRect = scoreSurface.get_rect(topleft=(5,0))

            return scoreSurface, scoreRect

        def highScoreText(highScore):
            highScoreSurface = HighScoreText.render(f"Personal Best: {highScore}", False, (0))
            highScoreRect = highScoreSurface.get_rect(topleft=(5,h-30))

            return highScoreSurface, highScoreRect

        def loseHealth(lostHealth):
            losthealthSurface = reduceHealthText.render(f"-{lostHealth}", False, (200,0,0))
            lostHealthRect = losthealthSurface.get_rect(center=(225,20))

            return losthealthSurface, lostHealthRect

        def deathText(size):
            DeathText = text.Text.loseHealth(size)
            deathTextSurface = DeathText.render("YOU DIED", False, (200,0,0))
            deathTextRect = deathTextSurface.get_rect(center=(w/2,40))

            return deathTextSurface, deathTextRect
        
        def currentSizeText(size):
            currentSizeSurface = CurrentSizeText.render(f"Current Size: {size}", False, (0))
            currentSizeRect = currentSizeSurface.get_rect(topleft=(5,40))

            return currentSizeSurface, currentSizeRect 
        
        def timerText(tick_time, max_time, x,y, size, Ymargin):
            TimerText = text.Text.timer(size)
            colour = (0,0,0)
            for i in range(0,max_time, 1):
                time_remaining = (max_time - tick_time)/100
                if time_remaining < 1.5 and time_remaining >= 0.5:
                    colour = (240,70,0)
                elif time_remaining < 0.5:
                    colour = (200,0,0)
                timerSurface = TimerText.render(f"{time_remaining}s", False, colour)
                timerRect = timerSurface.get_rect(center=(x,y-Ymargin))
                if timerRect.y <= 0:
                    timerRect = timerSurface.get_rect(center=(x,y+Ymargin+5))

                return timerSurface, timerRect
            
        def newPlayer(image):
            character1 = player(w,h,cw,ch,speed,f"{image}")

            return character1

        def Generate_Item(item, getItem, X, Y, notx1, noty1, notx2, noty2, tickTime):
                tickTime = tickTime
                if not ((X >= notx1 and Y >= noty1) and (X <= notx2 and Y <= noty2)):
                    itemFrame = item.spawn(X,Y) # Spawns item on random x and y positions
                    screen.blit(getItem,itemFrame) # Displays item
                else:
                    itemFrame = item.spawn(1000000,1000000)
                    tickTime = 0

                return itemFrame, tickTime
        
        def main():
            run = True
            ScreenCode = self.ScreenCode

            # PLAYER 1
            p = newPlayer(f"{dir}\\images\\idle.png")
            character = p.get_character()[1]
            spawnedPlayer = p.Spawn_Player(character, w/2, h/2)

            # COIN GENERATE
            coin1 = items.Items(50,50,'coin.png')
            getCoin1 = coin1.get_Item()
            coin2 = items.Items(50,50,'coin.png')
            getCoin2 = coin1.get_Item()
            bigCoin1 = items.Items(100,100,'coin.png')
            getBigCoin1 = bigCoin1.get_Item()

            # BOMB GENERATE
            bomb1 = items.Items(30,30,'bomb.png')
            getBomb1 = bomb1.get_Item()
            bigBomb1 = items.Items(75,75,'bomb.png')
            getBigBomb1 = bigBomb1.get_Item()
            explosionBomb = items.ExplosionBomb(50,50,f'{dir}\\images\\{"ExplosionBomb.png"}')
            getexplosionBomb = explosionBomb.get_ExplosionBomb()
            getExplosion = explosionBomb.get_explosion(150,150)

            # POWER-UP GENERATE
            sonic = items.Items(60,60,"sonic.png")
            getSonic = sonic.get_Item()
            downSize = items.Items(50,50,"SizeDown.png")
            getDownSize = downSize.get_Item()

            # OTHERS
            fatMan = items.Items(60,60,"runMan.png")
            getFatMan = fatMan.get_Item()
            fatMan2 = items.Items(60,60,"runMan2.png")
            getFatMan2 = fatMan2.get_Item()

            # VARIABLES/CONSTANTS
            p_score_count = 0
            difficulty = 300
            tick_time1 = 0
            tick_time2 = 0
            tick_time3 = 0
            tick_time4 = 0
            tick_time_bigBomb = 0
            tick_time_explosionBomb = 0
            tick_time_sonic = 0
            tick_time_fatMan = 0
            tick_time_sizeDown = 0
            textEvent = 0
            fati = 0
            fati2 = w
            deathtextEvent = 0
            highScoreCount = 0
            size = cw
            CurrentLargestSize = 0
            try:
                with open(f'{dir}\\Extra\\spHighScore') as file:
                    personalHighScore = int(file.read())
            except FileNotFoundError:
                print("File not found")
            try:
                with open(f'{dir}\\Extra\\spLargestSize') as file:
                    LargestSize = int(file.read())
            except FileNotFoundError:
                print("File not found")
            speed = 2
            lostHealth = 0
            #print(personalHighScore)

            Button = buttons.Button(40,30)
            screenColour = (48,69,41)

            # MAIN LOOP    
            while run:
                #print(size)
                #print(lostHealth)
                #print(speed)
                mouse = self.mouse.get_pos()
                scoreSurface = scoreText(p_score_count)[0]
                scoreRect = scoreText(p_score_count)[1]
                displayHighScore = highScoreText(personalHighScore)
                sizeSurface = currentSizeText(size)[0]
                sizeRect = currentSizeText(size)[1]
                tick_time_sizeDown += 1
                tick_time_fatMan += 1
                tick_time_sonic += 1
                tick_time_explosionBomb += 1
                tick_time_bigBomb += 1
                tick_time4 += 1
                tick_time3 += 1
                tick_time2 += 1
                tick_time1 += 1
                #print(tick_time)a
                screen.fill(screenColour)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LSHIFT:
                            speed = speed * 2
                            if speed > 4:
                                if tick_time_sonic > 1000:
                                    speed = 4
                    elif event.type == pygame.KEYUP:
                        if event.key == pygame.K_LSHIFT:
                            if speed > 2:
                                speed = speed / 2
                                if tick_time_sonic > 1000:
                                    speed = 2
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if w-50 <= mouse[0] <= w+40 and 0 <= mouse[1] <= h+30:
                            #print(ScreenCode)
                            ScreenCode = 0
                            #print(ScreenCode)
                            return ScreenCode

                # STAGE 0
                if tick_time1 >= 100:
                    coinGenerate = Generate_Item(coin1, getCoin1, randomX, randomY, spawnedPlayer.x - 10, spawnedPlayer.y - 10, spawnedPlayer.x+p.width + 10, spawnedPlayer.y+p.height + 10, tick_time1)
                    coinFrame1 = coinGenerate[0]
                    tick_time1 = coinGenerate[1]
                    displayTimer = timerText(tick_time1, 300, randomX, randomY, 15, 35)
                    screen.blit(displayTimer[0],displayTimer[1])
                    if coinFrame1.colliderect(spawnedPlayer): # if player collides with coin
                        for i in range(1,2,1): # Starts at 1, Stops at 2, Steps by 1
                            p.width += i # Player Width increases by i
                            p.height += i # Player Height increases by i
                            size += i
                        if size >= CurrentLargestSize:
                            CurrentLargestSize = size
                        tick_time1 = 0 # Resets tick_time (destroys coin)
                        p_score_count += 1
                        if p_score_count >= highScoreCount:
                            highScoreCount = p_score_count
                        print(f"You have collected {p_score_count} coins!")
                else:
                    randomX = rand.randint(0,w-75)
                    randomY = rand.randint(0,h-75)
                if tick_time1 >= difficulty:
                    tick_time1 = 0

                if tick_time4 >= 100:
                    coinGenerate = Generate_Item(coin2, getCoin2, randomX4, randomY4, spawnedPlayer.x - 10, spawnedPlayer.y - 10, spawnedPlayer.x+p.width + 10, spawnedPlayer.y+p.height + 10, tick_time4)
                    coinFrame2 = coinGenerate[0]
                    tick_time4 = coinGenerate[1]
                    displayTimer = timerText(tick_time4, 300, randomX4, randomY4, 15, 35)
                    screen.blit(displayTimer[0],displayTimer[1])
                    if coinFrame2.colliderect(spawnedPlayer): # if player collides with coin
                        for i in range(1,2,1): # Starts at 1, Stops at 2, Steps by 1
                            p.width += i # Player Width increases by i
                            p.height += i # Player Height increases by i
                            size += i
                        if size >= CurrentLargestSize:
                            CurrentLargestSize = size
                        tick_time4 = 0 # Resets tick_time (destroys coin)
                        p_score_count += 1
                        if p_score_count >= highScoreCount:
                            highScoreCount = p_score_count
                        print(f"You have collected {p_score_count} coins!")
                else:
                    randomX4 = rand.randint(0,w-75)
                    randomY4 = rand.randint(0,h-75)

                if tick_time4 >= difficulty:
                    tick_time4 = 0

                # STAGE 1

                if tick_time2 >= 75 and p_score_count >= 5:
                    bombGenerate = Generate_Item(bomb1, getBomb1, randomX2, randomY2, spawnedPlayer.x - 7, spawnedPlayer.y - 7, spawnedPlayer.x+p.width + 7, spawnedPlayer.y+p.height + 7, tick_time2)
                    bombFrame1 = bombGenerate[0]
                    tick_time2 = bombGenerate[1]
                    if bombFrame1.colliderect(spawnedPlayer): # if player collides with bomb
                        lostHealth += 10
                        if p.width < cw and p.height < ch:
                            p.width = cw
                            p.height = ch
                            size = cw
                        else:
                            p.width -= 5
                            p.height -= 5
                            size -= 5
                        p_score_count -= lostHealth
                        tick_time2 = 0
                        textEvent = 1
                        print(f"YOU LOST 10 COINS! ({p_score_count})")
                else:
                    randomX2 = rand.randint(0,w-75)
                    randomY2 = rand.randint(0,h-75)
                if tick_time2 >= 200:
                    tick_time2 = 0

                if tick_time3 >= 500 and p_score_count >= 5:
                    bigCoinGenerate = Generate_Item(bigCoin1, getBigCoin1, randomX3, randomY3, spawnedPlayer.x - 25, spawnedPlayer.y - 25, spawnedPlayer.x+p.width + 25, spawnedPlayer.y+p.height + 25, tick_time3)
                    bigCoin1Frame = bigCoinGenerate[0]
                    tick_time3 = bigCoinGenerate[1]
                    displayTimer = timerText(tick_time3, 650, randomX3, randomY3, 20, 60)
                    screen.blit(displayTimer[0],displayTimer[1])
                    if bigCoin1Frame.colliderect(spawnedPlayer): # if player collides with coin
                        for i in range(1,5,1): # Starts at 1, Stops at 2, Steps by 1
                            p.width += i # Player Width increases by i
                            p.height += i # Player Height increases by i
                            size += i
                        if size >= CurrentLargestSize:
                            CurrentLargestSize = size
                        tick_time3 = 0 # Resets tick_time (destroys coin)
                        p_score_count += 5
                        if p_score_count >= highScoreCount:
                            highScoreCount = p_score_count
                        print(f"You have collected {p_score_count} coins!")
                else:
                    randomX3 = rand.randint(0,w-75)
                    randomY3 = rand.randint(0,h-75)
                if tick_time3 >= 650:
                    tick_time3 = 0
            
                # STAGE 2

                if tick_time_bigBomb >= 50 and p_score_count >= 10:
                    bigBombGenerate = Generate_Item(bigBomb1, getBigBomb1, randomXbigBomb, randomYbigBomb, spawnedPlayer.x - 32, spawnedPlayer.y - 32, spawnedPlayer.x+p.width + 32, spawnedPlayer.y+p.height + 32, tick_time_bigBomb)
                    bigBombFrame1 = bigBombGenerate[0]
                    tick_time_bigBomb = bigBombGenerate[1]
                    if bigBombFrame1.colliderect(spawnedPlayer): # if player collides with coin
                        lostHealth += 30
                        if p.width < cw and p.height < ch:
                            p.width = cw
                            p.height = ch
                            size = cw
                        else:
                            p.width -= 15
                            p.height -= 15
                            size -= 15
                        textEvent = 1
                        tick_time_bigBomb = 0
                        p_score_count -= lostHealth
                        print(f"YOU LOST 30 COINS! ({p_score_count})")
                else:
                    randomXbigBomb = rand.randint(0,w-75)
                    randomYbigBomb = rand.randint(0,h-75)
                if tick_time_bigBomb >= 300:
                    tick_time_bigBomb = 0

                if (tick_time_sonic >= 2000) and p_score_count >= 15:
                    sonicGenerate = Generate_Item(sonic, getSonic, randomXsonic, randomYsonic, spawnedPlayer.x - 20, spawnedPlayer.y - 20, spawnedPlayer.x+p.width + 20, spawnedPlayer.y+p.height + 20, tick_time_sonic)
                    sonicFrame = sonicGenerate[0]
                    tick_time_sonic = sonicGenerate[1]
                    displayTimer = timerText(tick_time_sonic, 2500, randomXsonic, randomYsonic, 15, 40)
                    screen.blit(displayTimer[0],displayTimer[1])
                    if sonicFrame.colliderect(spawnedPlayer): # if player collides with coin
                        tick_time_sonic = 0
                        speed = speed * 2
                else:
                    randomXsonic = rand.randint(0,w-75)
                    randomYsonic = rand.randint(0,h-75)

                if tick_time_sonic >= 2500:
                    tick_time_sonic = 0

                # STAGE 3

                if tick_time_explosionBomb >= 50 and p_score_count >= 20:
                    explosionBombGenerate = Generate_Item(explosionBomb, getexplosionBomb, randomXexplosionBomb, randomYexplosionBomb, spawnedPlayer.x - 25, spawnedPlayer.y - 25, spawnedPlayer.x+p.width + 25, spawnedPlayer.y+p.height + 25, tick_time_explosionBomb)
                    explosionBombFrame = explosionBombGenerate[0]
                    tick_time_explosionBomb = explosionBombGenerate[1]
                    displayTimer = timerText(tick_time_explosionBomb, 140, randomXexplosionBomb, randomYexplosionBomb, 15, 35)
                    screen.blit(displayTimer[0],displayTimer[1])
                    if explosionBombFrame.colliderect(spawnedPlayer):
                        tick_time_explosionBomb = 140
                    if tick_time_explosionBomb >= 140:
                        bombExplostion = explosionBomb.spawn_explosion(randomXexplosionBomb, randomYexplosionBomb, 150, 150)
                        screen.blit(getExplosion,bombExplostion)
                        if bombExplostion.colliderect(spawnedPlayer):
                            p.width = cw
                            p.height = ch
                            size = cw
                            tick_time1 = 0
                            tick_time4 = 0
                            tick_time_bigBomb = 0
                            tick_time_sonic = 0
                            tick_time3 = 0
                            tick_time2 = 0
                            p_score_count = -1
                            tick_time_explosionBomb = 0
                            print(f"YOU WERE EXPLODED AND LOST EVERYTHING! ({p_score_count})")
                else:
                    randomXexplosionBomb = rand.randint(0,w-75)
                    randomYexplosionBomb = rand.randint(0,h-75)
                if tick_time_explosionBomb >= 150:
                    tick_time_explosionBomb = 0

                if tick_time_sizeDown >=50 and p_score_count >= 35:
                    sizeDownGenerate = Generate_Item(downSize, getDownSize, randomXsizeDown, randomYsizeDown, spawnedPlayer.x - 20, spawnedPlayer.y - 20, spawnedPlayer.x+p.width + 20, spawnedPlayer.y+p.height + 20, tick_time_sizeDown)
                    downSizeFrame = sizeDownGenerate[0]
                    tick_time_sizeDown = sizeDownGenerate[1]
                    displayTimer = timerText(tick_time_sizeDown, 150, randomXsizeDown, randomYsizeDown, 15, 25)
                    screen.blit(displayTimer[0],displayTimer[1])
                    if downSizeFrame.colliderect(spawnedPlayer):
                        if p.width > 20 and p.height > 20:
                            p.width -= 2
                            p.height -= 2
                            size -= 2
                        else:
                            pass
                else:
                    randomXsizeDown = rand.randint(0,w-75)
                    randomYsizeDown = rand.randint(0,h-75)
                if tick_time_sizeDown >= 150:
                    tick_time_sizeDown = 0




                if tick_time_fatMan >= 50 and p_score_count >= 30:
                    if randomxfatMan == 0:
                        fatManGenerate = Generate_Item(fatMan, getFatMan, fati, randomYfatMan, spawnedPlayer.x - 15, spawnedPlayer.y - 15, spawnedPlayer.x+p.width + 15, spawnedPlayer.y+p.height + 15, tick_time_fatMan)
                        fati += 10
                    elif randomxfatMan == w:
                        fatManGenerate = Generate_Item(fatMan2, getFatMan2, fati2, randomYfatMan, spawnedPlayer.x - 15, spawnedPlayer.y - 15, spawnedPlayer.x+p.width + 15, spawnedPlayer.y+p.height + 15, tick_time_fatMan)
                        fati2 -= 10
                    fatManFrame = fatManGenerate[0]
                    tick_time_fatMan = fatManGenerate[1]

                    if fatManFrame.colliderect(spawnedPlayer):
                        tick_time_fatMan = 500
                    if tick_time_fatMan >= 500:
                        p.width = cw
                        p.height = ch
                        size = cw
                        tick_time1 = 0
                        tick_time4 = 0
                        tick_time_bigBomb = 0
                        tick_time_sonic = 0
                        tick_time3 = 0
                        tick_time2 = 0
                        p_score_count = -1
                        tick_time_explosionBomb = 0
                        tick_time_fatMan = 0
                        fati = 0
                        print(f"YOU GOT ATE AND LOST EVERYTHING! ({p_score_count})")
                        
                else:
                    xBorders = [0,w]
                    randomxfatMan = rand.choice(xBorders)
                    randomYfatMan = rand.randint(10,h-10)
                if tick_time_fatMan >= 250:
                    tick_time_fatMan = 0
                    fati = 0
                    fati2 = w

                # PLAYER DIED
                if p_score_count < 0:
                    print("You have died")
                    p_score_count = 0
                    tick_time_sonic = 0
                    speed = 2
                    tick_time1 = 0 # Resets tick_time (destroys coin)
                    tick_time4 = 0
                    tick_time_bigBomb = 0
                    tick_time3 = 0
                    tick_time2 = 0
                    p.width = cw
                    p.height = ch
                    p.x = w/2
                    p.y = h/2
                    deathtextEvent = 1
                    tick_time_fatMan = 0
                    tick_time_sizeDown = 0
                    fati = 0
                    fati2 = w
                    size = cw
                    
                    if CurrentLargestSize > LargestSize:
                        LargestSize = CurrentLargestSize
                        print(f"New Size Score: {CurrentLargestSize}")
                        try:
                            with open(f'{dir}\\Extra\\spLargestSize', 'w') as file:
                                file.write(f"{CurrentLargestSize}")
                        except FileNotFoundError:
                            print("File not found")
                    print(f"Your top size: {CurrentLargestSize}")
                    CurrentLargestSize = 0

                    if highScoreCount > personalHighScore:
                        personalHighScore = highScoreCount
                        print(f"New High Score: {personalHighScore}")
                        try:
                            with open(f'{dir}\\Extra\\spHighScore', 'w') as file:
                                file.write(f"{highScoreCount}")
                        except FileNotFoundError:
                            print("File not found")
                    print(f"You Scored: {highScoreCount}")
                    highScoreCount = 0
                
                if textEvent >= 1 and textEvent <= 75:
                    textEvent += 1
                    displayHealth = loseHealth(lostHealth)
                    screen.blit(displayHealth[0],displayHealth[1])
                if textEvent > 75 and textEvent <= 125:
                    textEvent += 1
                    for i in 0.00,0.50,0.01:
                        displayHealth[1].y -= i
                        screen.blit(displayHealth[0],displayHealth[1])
                if textEvent > 125:
                    textEvent = 0
                    lostHealth = 0

                if deathtextEvent >= 1 and deathtextEvent <= 75:
                    deathtextEvent += 1
                    displayDeathText = deathText(50)
                    screen.blit(displayDeathText[0],displayDeathText[1])
                if deathtextEvent > 75 and deathtextEvent <= 150:
                    deathtextEvent += 1
                    for x in 0.00,0.90,0.01:
                        displayDeathText[1].y -= x
                        screen.blit(displayDeathText[0],displayDeathText[1])
                if deathtextEvent > 150:
                    deathtextEvent = 0
                    lostHealth = 0
                    textEvent = 0

                
                if game:
                    screen.blit(character,spawnedPlayer)

                keys = pygame.key.get_pressed()

                if keys[pygame.K_w]:
                    p.image = f"{dir}\\images\\idle.png"
                    character = p.get_character()[1]
                    spawnedPlayer = p.Spawn_Player(character, spawnedPlayer.x, spawnedPlayer.y)
                    screen.blit(character, spawnedPlayer)
                    spawnedPlayer.y -= speed # Moves PlayerBox Up
                if keys[pygame.K_s]:
                    p.image = f"{dir}\\images\\idle.png"
                    character = p.get_character()[1]
                    spawnedPlayer = p.Spawn_Player(character, spawnedPlayer.x, spawnedPlayer.y)
                    screen.blit(character, spawnedPlayer)
                    spawnedPlayer.y += speed # Moves PlayerBox Down
                if keys[pygame.K_a]:
                    spawnedPlayer.x -= speed # Moves PlayerBox left
                    p.change_image(p.x,p.y,"\\images\\player.png") # Grabs new image, and find x and y position of current player
                    p.image = p.image # Changes current image with new image
                    character = p.get_character()[1] # Sets new player character
                    spawnedPlayer = p.Spawn_Player(character, spawnedPlayer.x, spawnedPlayer.y) # Spawns in new player at same x and y position
                    screen.blit(character,spawnedPlayer) # Displays Character and CharacterBox
                    #print(p.image)
                if keys[pygame.K_d]:
                    p.change_image(p.x,p.y,"\\images\\playerR.png") # Grabs new image, and find x and y position of current player
                    p.image = p.image # Changes current image with new image
                    character = p.get_character()[1] # Sets new player character
                    spawnedPlayer = p.Spawn_Player(character, spawnedPlayer.x, spawnedPlayer.y)
                    screen.blit(character, spawnedPlayer)
                    #print(p.image)
                    spawnedPlayer.x += speed # Moves PlayerBox Right
                if keys[pygame.K_LSHIFT]:
                    if speed > 4:
                        if tick_time_sonic > 1000:
                            speed = 2

                if spawnedPlayer.left > w:
                    spawnedPlayer.right = 0
                elif spawnedPlayer.right < -10:
                    spawnedPlayer.x = w
                elif spawnedPlayer.top > h:
                    spawnedPlayer.bottom = 0
                elif spawnedPlayer.bottom < 0:
                    spawnedPlayer.top = h

                Button.quitButton(w-50, 0, mouse, (100,100,100), (170,170,170))[0]

                screen.blit(sizeSurface,sizeRect)
                screen.blit(scoreSurface,scoreRect)
                screen.blit(displayHighScore[0],displayHighScore[1])
                pygame.display.update()
                clock.tick(60)
                #print((spawnedPlayer.x,spawnedPlayer.y))
        return main()