from constants import *
from orb import *

class SlowMo(Orb):
    def power_up(self):
        pygame.event.post(pygame.event.Event(SLOW_MO))

class Coin(Orb):
    def __init__(self, x, y):
        self.x_loc = x
        self.y_loc = y
        self.orb_surface = pygame.image.load("assets/powerUps/coin.png").convert_alpha()
        self.orb_surface = pygame.transform.scale(self.orb_surface, ORB_DIM)
    def power_up(self):
        pygame.event.post(pygame.event.Event(COIN_COLLISION))

class FirePower(Orb):
    def __init__(self, x, y):
        self.x_loc = x
        self.y_loc = y
        self.orb_surface = pygame.image.load("assets/powerUps/fire_token.png").convert_alpha()
        self.orb_surface = pygame.transform.scale(self.orb_surface, ORB_DIM)
    def power_up(self):
        print("pewpew")

class Ghost(Orb):
    def power_up(self):
        print("BOO!")

class ScoreMult(Orb):
    def power_up(self):
        print("x2!")