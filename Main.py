import pygame

pygame.init

screen = pygame.display.set_mode([800, 800])
splashScreen = pygame.image.load('splashScreen.png')
splashScreen = pygame.transform.scale(splashScreen, pygame.display.get_surface().get_size())#Scales the splash screen to the size of the window


while True:
    screen.fill((75,75,75)) #screen filled with gray
    screen.blit(splashScreen, (0,0)) #splashscreen is drawn at the top left corner of the screen
    pygame.display.flip()         
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit(), sys.exit()


