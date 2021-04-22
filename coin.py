from constants import *
from orb import *

class Coin(Orb):
    def power_up(self):
        pygame.event.post(pygame.event.Event(COIN_COLLISION))