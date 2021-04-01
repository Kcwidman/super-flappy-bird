from constants import *
import random
class Pipe:

    def __init__(self, x):
        self.x_loc = x
        self.gap_loc = random.randrange(200, 600)
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