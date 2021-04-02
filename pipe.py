from constants import *
import random
class Pipe:

    def __init__(self, x):
        self.x_loc = x
        self.gap_loc = random.randrange(200, 700) #(200, 700)
        self.bot_pipe_surface = pygame.transform.scale(PIPE_SURFACE,(PIPE_WIDTH, FLOOR - self.gap_loc))
        self.top_pipe_surface = pygame.transform.scale(PIPE_SURFACE,(PIPE_WIDTH, self.gap_loc - PIPE_GAP))

        self.bot_pipe = self.bot_pipe_surface.get_rect(midtop = (self.x_loc, self.gap_loc))
        self.top_pipe = self.top_pipe_surface.get_rect(midtop = (self.x_loc, 0))
        self.top_pipe_surface = pygame.transform.flip(self.top_pipe_surface,False,True)

    def move(self):
        self.x_loc -= VEL
        self.bot_pipe.center = (self.x_loc, self.bot_pipe.center[1])
        self.top_pipe.center = (self.x_loc, self.top_pipe.center[1])

    def draw_pipe(self):
        SCREEN.blit(self.bot_pipe_surface, self.bot_pipe)
        SCREEN.blit(self.top_pipe_surface, self.top_pipe)
    
    def collide(self, bird):
        bird_mask = bird.get_mask()
        top_pipe_mask = pygame.mask.from_surface(self.top_pipe_surface)
        bot_pipe_mask = pygame.mask.from_surface(self.bot_pipe_surface)
        top_offset = (self.x_loc - bird.boundary.right + 5, self.top_pipe.top - round(bird.boundary.top))
        bot_offset = (self.x_loc - bird.boundary.right + 5, self.bot_pipe.top - round(bird.boundary.top))

        top_collide = bird_mask.overlap(top_pipe_mask, top_offset)
        bot_collide = bird_mask.overlap(bot_pipe_mask, bot_offset)

        if top_collide or bot_collide:
            return True
        else:
            return False