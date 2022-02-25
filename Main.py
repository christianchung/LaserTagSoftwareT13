from msilib.schema import CheckBox
from Database import Database
import sys
import pygame
import tkinter
import time # for the sleep function

#=====================================================================
#   Pass in database info from Database.py
#=====================================================================

# Initializes connection to Heroku and retrieves info from the database
database = Database()
database.RetrieveInfo()

#Initializes arrays to store the info from the database
idNumbers = []
firstNames = []
lastNames = []
codeNames = []

# Passes the database info from Database.py into here
database.PassInformation(idNumbers, firstNames, lastNames, codeNames)

# Test to make sure data is passed in correctly
print(idNumbers)
print(firstNames)
print(lastNames)
print(codeNames)

# Close connection to Heroku
database.CloseConnection()

#=====================================================================
#   Splash Screen
#=====================================================================

pygame.init()

screen = pygame.display.set_mode([800, 800])
splashScreen = pygame.image.load("splashScreen2.png")
width, height = pygame.display.get_surface().get_size()
splashScreenPosition = (0,0) # splashscreen is positioned at the top left corner of the screen

# following lines just prevent the splash screen from stretching if the window is rectangular
if(width > height):
    splashScreenPosition = ((width - height) / 2,0) # centers the image horizontally
    width = height
elif(height > width):
    splashScreenPosition = ((height - width) / 2,0) # centers the image vertically
    height = width

splashScreen = pygame.transform.scale(splashScreen, (width,height))#Scales the splash screen to the size of the window

splashScreenTimer = 0 
while (splashScreenTimer < 5 * 1): # splash screen is up for 1 second
    screen.fill((5,225,255)) # screen filled with cyan
    screen.blit(splashScreen, splashScreenPosition) 
    pygame.display.flip()         
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit(), sys.exit()
    splashScreenTimer += 1
    time.sleep(.2) # only sleep for .2 seconds so that the program doesn't freeze from not responding to events

#=====================================================================
#   Player Entry Screen
#=====================================================================
# light shade of the button
checkBoxColor = (115,115,115)
checkBoxColorHover = (75,75,75)
# print(pygame.font.get_fonts())        # gets all fonts on system
# initialize font to (defualt pygame font, fontSize)
font = pygame.font.Font(None, 30)

# other variables
checkMark = pygame.image.load("checkMark.png")
checkMark = pygame.transform.scale(checkMark, (30, 30))

checkBoxes = []
# saves 2 bools that will be set to True if the boxes are being hovered over or are selected
for x in range(40): # make 38 boxes (19 for each side)
    checkBoxes.append([False, False]) # left: hovered over ||| right: whether the check appears on the box or not

while True:
    screen.fill((0,195,0)) # fill screen with GREEN
    screen.fill((195,0,0), (0, 0, screen.get_width() / 2, screen.get_height())) # fill right side of screen with RED
    screen.fill((115,115,115), (0, 720, screen.get_width(), screen.get_height()/10)) # fill Bottom bar for Functions with GRAY
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit(), sys.exit()

        # check for mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
              
            # PROTOTYPE FOR CHECK BOXES - need to add color change or 'X' on click, as well as update a bool for each ID
            # QUIT on mouse click
            if 770 <= mouse[0] <= 770+28 and -2 <= mouse[1] <= 26:
                pygame.quit()

    mouse = pygame.mouse.get_pos() # store mouse position

    # change box color on hover
    if 770 <= mouse[0] <= 770+28 and -2 <= mouse[1] <= 26:
        pygame.draw.rect(screen,checkBoxColor,[770,2,28,28])
          
    else:
        pygame.draw.rect(screen,checkBoxColorHover,[770,2,28,28])

    # Team texts
    # add EDIT CURRENT GAME text
    text = font.render("Edit Current Game", 1, (5,5,5)) # Black text color
    screen.blit(text, (320, 5)) # position text on screen

    # add RED TEAM text
    text = font.render("Red Team", 1, (5,225,255)) # Cyan text color
    screen.blit(text, (150, 25))

    # add GREEN TEAM text
    text = font.render("Green Team", 1, (5,225,255))
    screen.blit(text, (550, 25))

    # draws boxes
    for x in range(20):

        # check boxes
        # left boxes
        if(checkBoxes[2 * x][0] == True):
            pygame.draw.rect(screen, (55,55,55), pygame.Rect(10, x * 33 + 56 ,15,15), 3)
        else:
            pygame.draw.rect(screen, (5,5,5), pygame.Rect(10, x * 33 + 56 ,15,15), 3)
        # right boxes
        if(checkBoxes[2* x + 1][0] == True):
            pygame.draw.rect(screen, (55,55,55), pygame.Rect(410, x * 33 + 56 ,15,15), 3)
        else:
            pygame.draw.rect(screen, (5,5,5), pygame.Rect(410, x * 33 + 56 ,15,15), 3) 

        # checks
        # left checks
        if(checkBoxes[2 * x][1] == True):
            screen.blit(checkMark, (6, x * 33 + 45))
        # right checks
        if(checkBoxes[2* x + 1][1] == True):
            screen.blit(checkMark, (406, x * 33 + 45))
        
        # small boxes
        screen.fill((255,255,255), (30, x * 33 + 50, 120, 30))
        screen.fill((255,255,255), (430, x * 33 + 50, 120, 30))

        # big boxes
        screen.fill((255,255,255), (155, x * 33 + 50, 240, 30))
        screen.fill((255,255,255), (555, x * 33 + 50, 240, 30))
        
    #writes text to boxes (currently only writes to red team side)
    counter = 0
    while counter < len(idNumbers) and counter < 20:
        text = font.render(codeNames[counter], 1, (5,5,5))
        text2 = font.render(firstNames[counter] + " " + lastNames[counter], 1, (5,5,5))
        screen.blit(text, (35, counter * 33 + 56))
        screen.blit(text2, (160, counter * 33 + 56))
        counter += 1


    pygame.display.flip() # keep at end of while loop
