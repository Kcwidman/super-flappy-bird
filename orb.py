from constants import *

#Orb is the basis for all of the powerups. It is incredibly important as the collision is handled here which allows the envents to be triggred in main.
class Orb:
    def __init__(self, x, y):
        self.x_loc = x
        self.y_loc = y
        self.orb_surface = None
        self.orb_surface = None

    def move(self):
        self.x_loc -= VEL
        
    #THis allows the orb to be created(all powerupw will be created with this function)
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
    
        #This is possiby the most important function for project 4, all collisions run through this with powerups
        #The power up will create different effects depending on which the bird collided with.
        if collide:
            self.power_up()
            return True
        else:
            return False
            
    def power_up(self):
        pass
