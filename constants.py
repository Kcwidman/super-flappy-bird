import pygame

CLOCK = pygame.time.Clock()
FPS = 30
VEL = 3

START = pygame.USEREVENT + 4

WIDTH, HEIGHT = 576, 900
SCREEN_DIM = (WIDTH, HEIGHT)
SCREEN = pygame.display.set_mode (SCREEN_DIM)

BG_SURFACE = pygame.image.load("assets/bg_day.png").convert()
BG_SURFACE = pygame.transform.scale(BG_SURFACE,(SCREEN_DIM))

BASE_HEIGHT = 200
BASE_SURFACE = pygame.image.load("assets/base.png").convert()
BASE_SURFACE = pygame.transform.scale(BASE_SURFACE,(WIDTH, 200))

PIPE_WIDTH = 50
PIPE_HEIGHT = 500
PIPE_SURFACE = pygame.image.load("assets/pipe.png").convert()
PIPE_SURFACE = pygame.transform.scale(PIPE_SURFACE,(PIPE_WIDTH, PIPE_HEIGHT))

        

GAME_OVER = pygame.USEREVENT + 1


# Bird Constants
BIRD_WIDTH = BIRD_HEIGHT = 50
BIRD_X = 50
BIRD_Y = int ( 576/2 - BIRD_HEIGHT/2 )
BIRD_IMAGE = pygame.image.load("assets/bird1.png").convert_alpha()
BIRD_SURFACE = BIRD_IMAGE
BIRD_BOUNDARY = BIRD_SURFACE.get_rect(center=(150,500))
BIRD_Y_CHANGE = 0