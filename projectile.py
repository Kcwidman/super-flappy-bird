from constants import *

class Projectile:
    def __init__(self, x, y):
        self.x_loc = x
        self.y_loc = y
        self.projectile_surface = pygame.image.load('assets/powerUps/fire_projectile.png').convert_alpha()
        self.projectile_boundary = self.projectile_surface.get_rect()
        
#simply draws the projectile sprite to the screen
    def draw_projectile(self):
        SCREEN.blit(self.projectile_surface, (self.x_loc, self.y_loc))

#move the projectile across the screen, opposite direction of the pipes
    def move_projectile(self):
        self.x_loc += VEL*2

#returns the pygame mask object that is used in the pygame collide functions
    def get_mask(self):
        return pygame.mask.from_surface(self.projectile_surface)