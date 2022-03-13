import sys
from database import Database
import pygame
import time # for the sleep function
import GameScreen

pygame.init()
screen = pygame.display.set_mode([800, 800])

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
#print(idNumbers)
#print(firstNames)
#print(lastNames)
#print(codeNames)

# def save(largeTextBoxes): #program saves on exit
#     idNumbers = []
#     firstNames = []
#     lastNames = []
#     codeNames = []
    
#     for x in range(len(largeTextBoxes)):
#         if(len(largeTextBoxes[x][0]) > 2): #names aren't saved if they're too short (at least 3 characters required)
#             if " " in largeTextBoxes[x][0][1:len(largeTextBoxes[x][0]) - 2]: #if the string contains a space that isn't at the start or end of the string
#                 idNumbers.append(x)
#                 firstNames.append(largeTextBoxes[x][0].split()[0])
#                 lastNames.append(largeTextBoxes[x][0].split()[len(largeTextBoxes[x][0].split()) - 1])
#                 codeNames.append(largeTextBoxes[x][0].split()[0][0:1] + largeTextBoxes[x][0].split()[1][0:1]) #codename is made from first initial + last initial
#             else:
#                 idNumbers.append(x)
#                 largeTextBoxes[x][0].replace(" ", "") 
#                 firstNames.append(largeTextBoxes[x][0])
#                 lastNames.append(" ")
#                 codeNames.append(largeTextBoxes[x][0][0:2]) #codename is made from first 2 letters of input name if no spaces
#     #### Add code to export finalized arrays before closing the connection and exiting the program ####   
#     database.deleteFunction()
#     database.insertFunction(idNumbers, firstNames, lastNames, codeNames)

#     ###################################################################################################


#For when a text box is deslected, happens if user clicks or presses enter while typing in a box
def deselect(selected):
    if(selected[1] == "smallTextBox" and selected[0][0].replace(" ", "") != ""): # if it's a small text box and has a valid id excluding spaces        
        database.LoadName(selected[0][0], largeTextBoxes[selected[2]])    

        print("loaded player!")  #change to show on screen later
    elif(selected[1] == "largeTextBox" and smallTextBoxes[selected[2]][0].replace(" ", "") != ""): # if it's a large text box and the small text box beside it has an ID
        database.deleteFunction(smallTextBoxes[selected[2]][0]) #deletes player at id of neighboring small text box
        if(selected[0][0] != "" and selected[0][0] != " "): #if the name is empty then the id associated with it gets deleted and not re-inserted
            database.insertFunction(smallTextBoxes[selected[2]][0], " ", " ", selected[0][0])

    selected = None
    


#=====================================================================
#   Splash Screen
#=====================================================================
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

# initialize font to (defualt pygame font, fontSize)
font = pygame.font.Font(None, 30)

# other variables
checkMark = pygame.image.load("checkMark.png")
checkMark = pygame.transform.scale(checkMark, (30, 30))
checkBoxes = []
smallTextBoxes = []
largeTextBoxes = []

for x in range(20): # make 20 left check boxes 
    checkBoxes.append([False, pygame.Rect(20, x * 33 + 56 ,15, 15)]) # left: whether the check appears on the box or not ||| right: stored the rect for drawing and mouse detection
for x in range(20): # make 20 right check boxes 
    checkBoxes.append([False, pygame.Rect(420, x * 33 + 56 ,15, 15)]) # left: whether the check appears on the box or not ||| right: stored the rect for drawing and mouse detection

for x in range(20): # make 20 left small text boxes
    smallTextBoxes.append(["", pygame.Rect(40, x * 33 + 50, 115, 30)]) 
for x in range(20): # make 20 right small text boxes 
    smallTextBoxes.append(["", pygame.Rect(440, x * 33 + 50, 115, 30)]) 

for x in range(20): # make 20 left large text boxes 
    largeTextBoxes.append(["", pygame.Rect(160, x * 33 + 50, 235, 30)]) 
for x in range(20): # make 20 right large text boxes 
    largeTextBoxes.append(["", pygame.Rect(560, x * 33 + 50, 235, 30)]) 

selected = [None, ""] #stores the currently selected textbox and the type of textbox (large or small) it is

#==================LOAD THE PLAYER LIST HERE==================#

#Change variable names to whatever fits best, all loading is done right here and the variables are not used again later

### load data into arrays here ###
# this loads up the IDs (never changes)
# for x in range(20):
#     if x < 10: # makes sure every text box on the left has 2 digits
#         smallTextBoxes[x][0] = ("0" + str(x)) 
#     else:
#         smallTextBoxes[x][0] = (str(x)) 
#     smallTextBoxes[x+20][0] = (str(x + 20)) #right text boxes
        
# # this loads up the text boxes
# for x in range(len(firstNames)):
#     if firstNames[x] == " ": # check if there's a first
#         largeTextBoxes[x] = "" #if not, insert blank
#     elif lastNames[x] == " ": # check if there's a last name for this entry
#         largeTextBoxes[idNumbers[x]][0] = firstNames[x] # if not, only insert first name
#     else:
#         largeTextBoxes[idNumbers[x]][0] = firstNames[x] + " " + lastNames[x]

#=============================================================#

while True:
    screen.fill((0,195,0)) # fill screen with GREEN
    screen.fill((195,0,0), (0, 0, screen.get_width() / 2, screen.get_height())) # fill right side of screen with RED
    screen.fill((115,115,115), (0, 720, screen.get_width(), screen.get_height()/10)) # fill Bottom bar for Functions with GRAY
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            #save(largeTextBoxes)
            # Close connection to Heroku
            database.CloseConnection()
            pygame.display.quit(), sys.exit()
        # KEY clicks
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F3:
                print("F3")
            elif event.key == pygame.K_F5:
                GameScreen.runGameScreen()
        # check for mouse click
        if event.type == pygame.MOUSEBUTTONDOWN:
            if selected != None:
                deselect(selected)
            clickFound = False #stops checking stuff if we've found what the mouse clicked
            for x in checkBoxes:
                if x[1].collidepoint(pygame.mouse.get_pos()):
                    clickFound = True
                    if x[0]:
                        x[0] = False
                        break
                    else:
                        x[0] = True
                        break
            if not clickFound:      
                for x in range(len(smallTextBoxes)):
                    if smallTextBoxes[x][1].collidepoint(pygame.mouse.get_pos()):
                        clickFound = True
                        selected = [smallTextBoxes[x], "smallTextBox", x]
                        break
            if not clickFound:
                for x in range(len(largeTextBoxes)):
                    if largeTextBoxes[x][1].collidepoint(pygame.mouse.get_pos()):
                        clickFound = True
                        selected = [largeTextBoxes[x], "largeTextBox", x]
                        break
        if event.type == pygame.KEYDOWN and selected[0] != None:
            if event.key == pygame.K_RETURN:
                if selected != None:
                    deselect(selected)
            elif event.key == pygame.K_BACKSPACE:
                selected[0][0] = selected[0][0][:-1]
            else:
                if selected[1] == "smallTextBox":
                    if len(selected[0][0]) < 9:
                        selected[0][0] += event.unicode
                elif selected[1] == "largeTextBox":
                    if len(selected[0][0]) < 18:
                        selected[0][0] += event.unicode

    # Team TEXTS
    # add EDIT CURRENT GAME text
    text = font.render("Edit Current Game", 1, (5,5,5)) # Black text color
    screen.blit(text, (315, 5)) # position text on screen

    # add RED TEAM text
    text = font.render("Red Team", 1, (5,225,255)) # Cyan text color
    screen.blit(text, (150, 25))

    # add GREEN TEAM text
    text = font.render("Green Team", 1, (5,225,255))
    screen.blit(text, (550, 25))

    # add F3 BOX
    pygame.draw.rect(screen, (5,5,5), pygame.Rect(265, 723, 80, 75), 2, 10)

    # add F3 and RUN GAME text
    text = font.render("F3", 1, (5,5,5))
    screen.blit(text, (280, 730))
    text = font.render("Empty", 1, (5,5,5))
    screen.blit(text, (280, 750))
    text = font.render("Task", 1, (5,5,5))
    screen.blit(text, (280, 770))

    # add F5 BOX
    pygame.draw.rect(screen, (5,5,5), pygame.Rect(365, 723, 80, 75), 2, 10)

    # add F5 and GAME SCREEN text
    text = font.render("F5", 1, (5,5,5))
    screen.blit(text, (370, 730))
    text = font.render("Game", 1, (5,5,5))
    screen.blit(text, (370, 750))
    text = font.render("Screen", 1, (5,5,5))
    screen.blit(text, (370, 770))

    # add text saving info
    smallFont = pygame.font.Font(None, 18)
    # pygame doesn't support multiple lines, must blit two different strings
    text = smallFont.render("Names save to database when program closes", 1, (0,0,0))
    screen.blit(text, (0,0))
    text = smallFont.render("and load from database when program opens", 1, (0,0,0))
    screen.blit(text, (0,12))

    # Checked Player Arrays for Game Screen (!!! *FIX* !!!)
    redPlayers = ["Trey", "Mark", "John"]
    greenPlayers = ["Tery", "Bob", "George"]
    
    # draws boxes
    for x in range(20):
        
        # check boxes
        # left boxes
        if checkBoxes[x][1].collidepoint(pygame.mouse.get_pos()): #checks if mouse hovering over
            pygame.draw.rect(screen, (55,55,55), checkBoxes[x][1], 2, 3)
        else:
            pygame.draw.rect(screen, (5,5,5), checkBoxes[x][1], 2, 3)
        # right boxes
        if checkBoxes[x + 20][1].collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, (55,55,55), checkBoxes[x + 20][1], 2, 3)
        else:
            pygame.draw.rect(screen, (5,5,5), checkBoxes[x + 20][1], 2, 3)

        # checks
        # left checks
        if(checkBoxes[x][0] == True):
            screen.blit(checkMark, (16, x * 33 + 45))
        # right checks
        if(checkBoxes[x + 20][0] == True):
            screen.blit(checkMark, (416, x * 33 + 45))
        
        # small text boxes
        screen.fill((255,255,255), smallTextBoxes[x][1])
        text = font.render(smallTextBoxes[x][0], 1, (5,5,5))
        screen.blit(text, text.get_rect(center=(smallTextBoxes[x][1].center)))

        screen.fill((255,255,255), smallTextBoxes[x + 20][1])
        text = font.render(smallTextBoxes[x + 20][0], 1, (5,5,5))
        screen.blit(text, text.get_rect(center=(smallTextBoxes[x + 20][1].center)))

        # large text boxes
        screen.fill((255,255,255), largeTextBoxes[x][1])
        text = font.render(largeTextBoxes[x][0], 1, (5,5,5))
        screen.blit(text, text.get_rect(center=(largeTextBoxes[x][1].center)))

        screen.fill((255,255,255), largeTextBoxes[x + 20][1])
        text = font.render(largeTextBoxes[x + 20][0], 1, (5,5,5))
        screen.blit(text, text.get_rect(center=(largeTextBoxes[x + 20][1].center)))

    pygame.display.flip() # keep at end of while loop