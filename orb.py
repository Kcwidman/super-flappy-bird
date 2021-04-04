from constants import *

class Orb:
    def __init__(self, x, y):
        self.x_loc = x
        self.y_loc = y
        self.orb_surface = pygame.image.load("assets/coin.png").convert_alpha()
        self.orb_surface = pygame.transform.scale(self.orb_surface, ORB_DIM)

    def move(self):
        self.x_loc -= VEL

    def draw_orb(self):
        SCREEN.blit(self.orb_surface, (self.x_loc, self.y_loc))

    def collide(self, bird):
#SET MASKS
        bird_mask = bird.get_mask()
        orb_mask = pygame.mask.from_surface(self.orb_surface)
#FIND OFFSET
        offset = (self.x_loc - bird.x_loc, self.y_loc - round(bird.y_loc))
#CHECK AND RETURN FOR OVERLAP OF MASKS
        collide = bird_mask.overlap(orb_mask, offset)

        if collide:
            self.power_up()
            return True
        else:
            return False
            
    def power_up(self):
        pass