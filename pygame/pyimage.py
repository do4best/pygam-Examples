import pygame #pygam import
pygame.init() # pygame initialize
screen = pygame.display.set_mode((500, 500)) #display mode is set
pygame.display.set_caption('pygame') # set the title
clock = pygame.time.Clock() # clock time
stop = False # stop it false
while not stop: # untill it stop
    for event in pygame.event.get(): # when the event to get
        print(event)
        if event.type == pygame.QUIT:  # when quit
            stop = True # it should be stop
    pygame.display.update() # update the display
    clock.tick(60) # update the click as per argument given

pygame.quit()
quit()