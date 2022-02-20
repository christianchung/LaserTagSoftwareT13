import pygame

pygame.init

screen = pygame.display.set_mode([720, 480])


splashScreen = pygame.image.load('splashScreen.png')
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


while True:
    screen.fill((75,75,75)) #screen filled with gray
    screen.blit(splashScreen, splashScreenPosition) 
    pygame.display.flip()         
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit(), sys.exit()


