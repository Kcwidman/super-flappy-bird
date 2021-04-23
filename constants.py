import pygame

#global constants
CLOCK = pygame.time.Clock()
FPS = 60
VEL = 2 #2
GAME_OVER = pygame.USEREVENT + 1

#window constants
WIDTH, HEIGHT = 600, 900
SCREEN_DIM = (600, HEIGHT)
SCREEN = pygame.display.set_mode (SCREEN_DIM)

#background constants
BG_SURFACE = pygame.image.load("assets/bg_day.png").convert()
BG_SURFACE = pygame.transform.scale(BG_SURFACE,(SCREEN_DIM))

#base constants
BASE_HEIGHT = 100
BASE_SURFACE = pygame.image.load("assets/base.png").convert_alpha()
BASE_SURFACE = pygame.transform.scale(BASE_SURFACE,(WIDTH, BASE_HEIGHT))

#pipe constants
PIPE_WIDTH = 50
PIPE_GAP = 120
PIPE_SPACING = 200
PIPE_HEIGHT = 500
PIPE_SURFACE = pygame.image.load("assets/pipe.png").convert()
PIPE_SURFACE = pygame.transform.scale(PIPE_SURFACE, (PIPE_WIDTH, 600))

# Bird Constants
BIRD_START_X_LOC = 150
BIRD_START_Y_LOC = 450
BIRD_WIDTH = BIRD_HEIGHT = 50
BIRD_SURFACE = pygame.image.load("assets/bird_up.png").convert_alpha()
FALLING_ACC = 0.4 #0.4
TERMINAL_VEL = 9 #9
JUMP_HEIGHT = -6 #-6

#Orb constants
ORB_DIM = (30, 30)
SLOW_MO = pygame.USEREVENT + 3
COIN_COLLISION = pygame.USEREVENT + 2
FIRE_POWER = pygame.USEREVENT + 4
GHOST = pygame.USEREVENT + 5
SCORE_MULT = pygame.USEREVENT + 6

#derived constants
FLOOR = HEIGHT - BASE_HEIGHT
