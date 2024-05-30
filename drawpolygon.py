import sys

import pygame # import pygame
pygame.init() # initialize pygame
screen = pygame.display.set_mode((500, 500)) # decide screen size
pygame.display.set_caption('Draw polygon')    # set caption for title
points = []  # initialize point list
while True: # point the condation
    for event in pygame.event.get(): # a loop for event.get()
        if event.type == pygame.QUIT: # if the event type is quit
            exit()  # exit immediatly
        if event.type == pygame.MOUSEBUTTONDOWN: # and another condation if there is mousebutton is pressed
            points.append(event.pos) # when pressed it should be append it
    screen.fill((255, 255, 255)) # screen color
    if len(points) >= 3: # if there is there points
        pygame.draw.polygon(screen, (0, 255, 255), points) # polygone color
    for point in points:
        pygame.draw.circle(screen, (0, 255, 0), point, 5)# point color

    pygame.display.update()