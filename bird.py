import pygame
from constants import *

class Bird:
    birdDown = pygame.image.load('assets/bird3.png').convert_alpha()
    birdCenter = pygame.image.load('assets/bird2.png').convert_alpha()
    birdUp = pygame.image.load('assets/bird1.png').convert_alpha()
    birdFrame = [birdDown, birdCenter, birdUp]
    tick_count = 0
    falling_vel = 0
    rot_angle = 0
    frame_index = 0
    boundary = BIRD_SURFACE.get_rect(center=(150, 500))

    def animate_bird(self):
        self.tick_count += 1
        if self.tick_count % 3 == 0:
            self.frame_index = (self.frame_index + 1) % 3
        rotoBird = pygame.transform.rotozoom(self.birdFrame[self.frame_index], max(-self.falling_vel * 5, -70), 1)
        return rotoBird

    def draw_bird(self):
        rotoBird = self.animate_bird()
        SCREEN.blit(rotoBird, self.boundary)

    def bird_fall(self):
        self.rot_angle = -self.falling_vel * 5
        self.falling_vel += FALLING_ACC
        self.boundary.centery += self.falling_vel

    def jump_bird(self):
        self.falling_vel = JUMP_HEIGHT

