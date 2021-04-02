import pygame
from constants import *

class Bird:

    falling_vel = 0
    rot_angle = 0
    boundary = BIRD_SURFACE.get_rect(center=(150,500))

    def animate_bird(self):
        rotoBird = pygame.transform.rotozoom(BIRD_SURFACE, max(-self.falling_vel * 5, -70), 1)
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

