from constants import *
from orb import *

# slow motion powerup. Not implemented in the working version of the game
class SlowMo(Orb):
    def power_up(self):
        pygame.event.post(pygame.event.Event(SLOW_MO))

# loads an image of coin. Checks for collision with coin
class Coin(Orb):
    def __init__(self, x, y):
        self.x_loc = x
        self.y_loc = y
        self.orb_surface = pygame.image.load("assets/powerUps/coin.png").convert_alpha()
        self.orb_surface = pygame.transform.scale(self.orb_surface, ORB_DIM)
    def power_up(self):
        pygame.event.post(pygame.event.Event(COIN_COLLISION))

# loads an image of fire. Checks for collision with fire
class FirePower(Orb):
    def __init__(self, x, y):
        self.x_loc = x
        self.y_loc = y
        self.orb_surface = pygame.image.load("assets/powerUps/fire_token.png").convert_alpha()
        self.orb_surface = pygame.transform.scale(self.orb_surface, ORB_DIM)
    def power_up(self):
        pygame.event.post(pygame.event.Event(FIRE_POWER))

# loads an image of ghost. Checks for collision with ghost
class Ghost(Orb):
    def __init__(self, x, y):
        self.x_loc = x
        self.y_loc = y
        self.orb_surface = pygame.image.load("assets/powerUps/ghost_token.png").convert_alpha()
        self.orb_surface = pygame.transform.scale(self.orb_surface, ORB_DIM)
    def power_up(self):
        pygame.event.post(pygame.event.Event(GHOST))

# loads an image of the star. Checks for collision with star
class ScoreMult(Orb):
    def __init__(self, x, y):
        self.x_loc = x
        self.y_loc = y
        self.orb_surface = pygame.image.load("assets/powerUps/mult_token.png").convert_alpha()
        self.orb_surface = pygame.transform.scale(self.orb_surface, ORB_DIM)
    def power_up(self):
        pygame.event.post(pygame.event.Event(SCORE_MULT))