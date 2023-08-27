import pygame

# All the constants are defined here
WIDTH, HEIGHT = 800,800
ROWS, COLS = 8,8
SQUARE_SIZE = WIDTH//COLS
CROWN = pygame.transform.scale(pygame.image.load("checkers/assets/crown.png"), (45,25))

RED = (255,0,0)
WHITE = (255,255,255)
GREY = (128,128,128)
GREYISH = (192,192,192)
BLACK = (0,0,0)
BLUE = (0,0,255)