import pygame
import sys

# this class have sounds source that will be used in the game.py
class Sound:

    def __init__(self):
        self.score_sound = pygame.mixer.Sound('assets\point.ogg')
        self.bg_music = pygame.mixer.music.load('assets\\background_music.mp3')
        self.hit = pygame.mixer.Sound('assets\hit.ogg')
        # self.coin_sound = pygame.mixer.Sound('assets\coin_sound.mp3')
        