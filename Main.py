import pygame
import time #for the sleep function

pygame.init

screen = pygame.display.set_mode([800, 800])


splashScreen = pygame.image.load("splashScreen.png")
width, height = pygame.display.get_surface().get_size()
splashScreenPosition = (0,0) #splashscreen is positioned at the top left corner of the screen

#following lines just prevent the splash screen from stretching if the window is rectangular
if(width > height):
    splashScreenPosition = ((width - height) / 2,0) #centers the image horizontally
    width = height
elif(height > width):
    splashScreenPosition = ((height - width) / 2,0) #centers the image vertically
    height = width

splashScreen = pygame.transform.scale(splashScreen, (width,height))#Scales the splash screen to the size of the window

#splash screen
splashScreenTimer = 0 
while (splashScreenTimer < 5 * 1): #splash screen is up for 1 second
    screen.fill((75,75,75)) #screen filled with gray
    screen.blit(splashScreen, splashScreenPosition) 
    pygame.display.flip()         
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit(), sys.exit()
    splashScreenTimer += 1
    time.sleep(.2) #only sleep for .2 seconds so that the program doesn't freeze from not responding to events

#everything after the splash screen
while True:
    screen.fill((0,200,0)) #fill screen with red
    screen.fill((200,0,0), (0, 0, screen.get_width() / 2, screen.get_height())) #fill right side of screen with screen
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit(), sys.exit()

    #draws boxes
    for x in range(20):
        #small boxes
        screen.fill((255,255,255), (30, x * 37 + 50, 120, 34))
        screen.fill((255,255,255), (430, x * 37 + 50, 120, 34))

        #big boxes
        screen.fill((255,255,255), (155, x * 37 + 50, 240, 34))
        screen.fill((255,255,255), (555, x * 37 + 50, 240, 34))




    pygame.display.flip() #keep at end of while loop

