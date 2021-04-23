from constants import *

class Base:
    x_loc = 0
    y_loc = FLOOR

    def draw(self):
        self.x_loc -= VEL
        SCREEN.blit(BASE_SURFACE,(self.x_loc, self.y_loc))
        SCREEN.blit(BASE_SURFACE,(self.x_loc + WIDTH, self.y_loc))
        if self.x_loc <= -WIDTH:
            self.x_loc = 0
    
    def collide(self, bird):
# #SET MASKS
#         bird_mask = bird.get_mask()
#         base_mask = pygame.mask.from_surface(BASE_SURFACE)
# #FIND OFFSET
#         offset = (self.x_loc - bird.x_loc, self.y_loc - round(bird.y_loc))
# #CHECK AND RETURN FOR OVERLAP OF MASKS
#         collide = bird_mask.overlap(base_mask, offset)

#         if collide:
#             return True
#         else:
#             return False
        if bird.y_loc + bird.bird_img.get_height() + 9 >= self.y_loc:
            return True
        else:
            return False