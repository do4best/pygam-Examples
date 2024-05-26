import sys
from random import randint
from pygame.locals import *

import pygame
pygame.init()
screen = pygame.display.set_mode((500, 500))
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    rand_col = (randint(0, 255), randint(0, 255), randint(0, 255))
    screen.lock()
    for _ in range(100):
        rand_pos = (randint(0, 639), randint(0, 479))
        screen.set_at(rand_pos,rand_col)
    screen.unlock()
    pygame.display.update()
