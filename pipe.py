from constants import *
import random
class Pipe:

    def __init__(self, x, gap_loc):
        self.x_loc = x
        #self.passed
        if gap_loc == 0: self.gap_loc = random.randrange(250, 650) #(200, 700)
        self.bot_pipe_end = self.gap_loc
        self.top_pipe_end = self.gap_loc - PIPE_GAP - PIPE_SURFACE.get_height()
        self.bot_pipe_surface = PIPE_SURFACE
        self.top_pipe_surface = pygame.transform.flip(PIPE_SURFACE,False,True)
        self.passed = False

    def move(self):
        self.x_loc -= VEL

    def draw_pipe(self):
        SCREEN.blit(self.bot_pipe_surface, (self.x_loc, self.bot_pipe_end))
        SCREEN.blit(self.top_pipe_surface, (self.x_loc, self.top_pipe_end))
    
    def collide(self, bird):
#SET MASKS
        bird_mask = bird.get_mask()
        top_pipe_mask = pygame.mask.from_surface(self.top_pipe_surface)
        bot_pipe_mask = pygame.mask.from_surface(self.bot_pipe_surface)
#FIND OFFSETS
        top_offset = (self.x_loc - bird.x_loc, self.top_pipe_end - round(bird.y_loc))
        bot_offset = (self.x_loc - bird.x_loc, self.bot_pipe_end - round(bird.y_loc))
#CHECK AND RETURN FOR OVERLAP OF MASKS
        top_collide = bird_mask.overlap(top_pipe_mask, top_offset)
        bot_collide = bird_mask.overlap(bot_pipe_mask, bot_offset)

        if top_collide or bot_collide:  
            return True
        else:
            return False
    
    def scorecal(self,bird):
        if self.x_loc  <= bird.x_loc and self.passed == False:
            self.passed = True
            return True
        else:
            return False