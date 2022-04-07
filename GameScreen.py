import sys
import pygame
import time # for the sleep function

pygame.init()

screen = pygame.display.set_mode([800, 800])
#=====================================================================
#   CountDown Timer
#=====================================================================
def countdownTimer(startOrEnd): #true if start, false if end     
    if startOrEnd:
        matchText = pygame.image.load("matchStartsIn.png")
    else:
        matchText = pygame.image.load("matchEndIn.png")
    timer5 = pygame.image.load("matchStart5.png")
    timer4 = pygame.image.load("matchStart4.png")
    timer3 = pygame.image.load("matchStart3.png")
    timer2 = pygame.image.load("matchStart2.png")
    timer1 = pygame.image.load("matchStart1.png")
    width, height = pygame.display.get_surface().get_size()
    timerPosition = (0,0) # timer words are positioned at the top left corner of the screen
    timerNumPosition = (0,0) # timer nums are positioned at the top left corner of the screen

    # prevent the splash screen from stretching if the window is rectangular
    if(width > height):
        timerPosition = ((width - height) / 2,0) # centers the image horizontally
        timerNumPosition = ((width - height) / 2,0)
        width = height
    elif(height > width):
        timerPosition = ((height - width) / 2,0) # centers the image vertically
        timerNumPosition = ((width - height) / 2,0)
        height = width

    # Scales the countdown text and nums to the size of the window
    matchText = pygame.transform.scale(matchText, (width,height)) 
    timer5 = pygame.transform.scale(timer5, (width,height))
    timer4 = pygame.transform.scale(timer4, (width,height))
    timer3 = pygame.transform.scale(timer3, (width,height))
    timer2 = pygame.transform.scale(timer2, (width,height))
    timer1 = pygame.transform.scale(timer1, (width,height))

    matchTimer = 0 

    while (matchTimer < 15 * 1): # splash screen is up for 1 second
        screen.fill((5,225,255)) # screen filled with cyan
        if(matchTimer < 4): screen.blit(matchText, timerPosition) 
        elif(matchTimer > 4 and matchTimer < 6): screen.blit(timer5, timerNumPosition) 
        elif(matchTimer > 6 and matchTimer < 8): screen.blit(timer4, timerNumPosition) 
        elif(matchTimer > 8 and matchTimer < 10): screen.blit(timer3, timerNumPosition) 
        elif(matchTimer > 10 and matchTimer < 12): screen.blit(timer2, timerNumPosition) 
        elif(matchTimer > 12 and matchTimer < 14): screen.blit(timer1, timerNumPosition) 
        pygame.display.flip()         
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit(), sys.exit()
        matchTimer += 1
        time.sleep(0.56)

#these are just here to make starting and ending more intutive than passing a bool to the countdowntimer function
def startGame():
    countdownTimer(True)
def endGame():
    countdownTimer(False)

#=====================================================================
#   Game Screen
#=====================================================================
def runGameScreen(redPlayers, greenPlayers):

    # light shade of the button
    checkBoxColor = (115,115,115)
    checkBoxColorHover = (75,75,75)
    # initialize font to (defualt pygame font, fontSize)
    font = pygame.font.Font(None, 30)

    # other variables
    iteratorCheck = True
    isGameStart = False
    startTime = 0
    smallTextBoxes = []
    largeTextBoxes = []

    # Game Timer
    
    

    # for x in range(20): # make 20 left check boxes 
    #     checkBoxes.append([False, pygame.Rect(20, x * 33 + 56 ,15, 15)]) # left: whether the check appears on the box or not ||| right: stored the rect for drawing and mouse detection
    # for x in range(20): # make 20 right check boxes 
    #     checkBoxes.append([False, pygame.Rect(420, x * 33 + 56 ,15, 15)]) # left: whether the check appears on the box or not ||| right: stored the rect for drawing and mouse detection

    # for x in range(20): # make 20 left small text boxes
    #     smallTextBoxes.append(["", pygame.Rect(40, x * 33 + 50, 115, 30)]) 
    # for x in range(20): # make 20 right small text boxes 
    #     smallTextBoxes.append(["", pygame.Rect(440, x * 33 + 50, 115, 30)]) 

    # for x in range(20): # make 20 left large text boxes 
    #     largeTextBoxes.append(["", pygame.Rect(160, x * 33 + 50, 235, 30)]) 
    # for x in range(20): # make 20 right large text boxes 
    #     largeTextBoxes.append(["", pygame.Rect(560, x * 33 + 50, 235, 30)]) 

    # selected = [None, ""] #stores the currently selected textbox and the type of textbox (large or small) it is

    #=============================================================#
    #   LOOP
    #=============================================================#

    while iteratorCheck == True:
        screen.fill((5,225,255)) # fill screen with CYAN
        # %%screen.fill((100,100,100), (0, 0, screen.get_width() / 2, screen.get_height())) # leaderboard
        screen.fill((115,115,115), (0, 720, screen.get_width(), screen.get_height()/10)) # fill Bottom bar for Functions with GRAY

        # add GAME ACTIONS BOX
        screen.fill((255,255,255), pygame.Rect(50, 50, 700, 600))
        pygame.draw.rect(screen, (25,25,25), pygame.Rect(45, 45, 705, 611), 10, 10) # Full box
        pygame.draw.rect(screen, (25,25,25), pygame.Rect(45, 45, 705, 280), 10, 10) # Team divider
        pygame.draw.rect(screen, (25,25,25), pygame.Rect(45, 45, 705, 570), 10, 10) # Time divider

        # add F3 BOX
        pygame.draw.rect(screen, (5,5,5), pygame.Rect(265, 723, 80, 75), 2, 10)

        # add F3 and RUN GAME text
        text = font.render("F3", 1, (5,5,5))
        screen.blit(text, (280, 730))
        text = font.render("Run", 1, (5,5,5))
        screen.blit(text, (280, 750))
        text = font.render("Game", 1, (5,5,5))
        screen.blit(text, (280, 770))

        # add F5 BOX
        pygame.draw.rect(screen, (5,5,5), pygame.Rect(365, 723, 80, 75), 2, 10)

        # add F5 and BACK text
        text = font.render("F5", 1, (5,5,5))
        screen.blit(text, (375, 740))
        text = font.render("Back", 1, (5,5,5))
        screen.blit(text, (375, 760))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit(), sys.exit()

            # check for KEY clicks
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F3:
                    startGame()
                    isGameStart = True
                    startTime = int(time.time())
                if event.key == pygame.K_F5:
                    iteratorCheck = False

            # check for MOUSE click
            if event.type == pygame.MOUSEBUTTONDOWN:
                clickFound = False #stops checking stuff if we've found what the mouse clicked

        # add EDIT CURRENT GAME text
        text = font.render("Game Stats", 1, (5,5,5)) # Black text color
        screen.blit(text, (320, 10)) # position text on screen

        # add Red Team
        text = font.render("RED TEAM", 1, (5,5,5)) # Black text color
        screen.blit(text, (120, 70)) # position text on screen

        # add Players (Red)
        playerLocation = 100
        for x in redPlayers[:6]:
            text = font.render(x, 1, (5,5,5)) # Black text color
            screen.blit(text, (120, playerLocation)) # position text on screen
            playerLocation = playerLocation + 25

        # add Green Team
        text = font.render("GREEN TEAM", 1, (5,5,5)) # Black text color
        screen.blit(text, (540, 70)) # position text on screen

        # add Players (Green)
        playerLocation = 100
        for x in greenPlayers[:6]:
            text = font.render(x, 1, (5,5,5)) # Black text color
            screen.blit(text, (540, playerLocation)) # position text on screen
            playerLocation = playerLocation + 25
        
        # add Current Game Action
        text = font.render("Current Game Action", 1, (5,5,5)) # Black text color
        screen.blit(text, (280, 340)) # position text on screen

        # add Time Remaining
        text = font.render("Time Remaining:", 1, (5,5,5)) # Black text color
        screen.blit(text, (120, 620)) # position text on screen

        timeElapsed = 600 - (int(time.time()) - startTime) #10 minutes (600 seconds) - the time since the timer was started
        minutes = int(timeElapsed / 60) #minutes left
        seconds = timeElapsed % 60 #seconds left
        if seconds < 10: #makes sure a time like 2:1 isn't shown instead of 2:01
            remainingTime = str(minutes) + ":0" + str(seconds) #string to use in font.render (this one adds the extra 0)
        else:
            remainingTime = str(minutes) + ":" + str(seconds) #string to use in font.render

        if(isGameStart):
            if (minutes < 1 and seconds < 9): #if game timer has 8 seconds left(allow time for match end slide), call endGame() function
                isGameStart = False
                endGame()
            else:
               text = font.render(remainingTime,  1, (5,5,5))
        else:
            text = font.render("10:00", 1, (5,5,5)) # Black text color
        screen.blit(text, (540, 620)) # position text on screen

        pygame.display.flip() # keep at end of while loop
