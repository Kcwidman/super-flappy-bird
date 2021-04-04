import sys
from constants import *
from bird import *
from base import *
from pipe import *
from score import *
class Game:

    def __init__(self):
        pygame.key.set_repeat(100)
        pygame.init()
        pygame.display.set_caption("Flappy Bird")
        self.base = Base()
        self.birdObj = Bird()
        self.pipelist = []
        self.Score = Score()
        self.easy_mode = False

    def draw_window(self):
        SCREEN.blit(BG_SURFACE,(0,0))
        for pipe in self.pipelist:
            pipe.draw_pipe()
        self.base.draw()
        self.birdObj.draw_bird()
        self.Score.score_display()

    def generate_pipes(self):
    #GENERATE PIPES
        if len(self.pipelist) == 0:
            for i in range (1, 5):#(1,5)
                self.pipelist.append(Pipe(WIDTH + i*PIPE_SPACING))#WIDTH + i*PIPE_SPACING
    #DELETE PIPES WHEN THEY GO OFF SCREEN
        if self.pipelist[0].x_loc <= -PIPE_WIDTH:
            self.pipelist.append(Pipe(WIDTH + PIPE_SPACING + self.pipelist[0].x_loc))
            self.pipelist.pop(0)
        
        
    def game_loop(self, start):
        self.draw_window()
        pygame.display.update()
        if start:
    #Affect pipes
                self.generate_pipes()
                for pipe in self.pipelist:
                    if pipe.scorecal(self.birdObj) == True:
                        self.Score.score += 1
                for pipe in self.pipelist:
                    if pipe.collide(self.birdObj) == True:
                        pygame.event.post(pygame.event.Event(GAME_OVER))
                    pipe.move()
    #Check for base collision
                if self.base.collide(self.birdObj) == True:
                    pygame.event.post(pygame.event.Event(GAME_OVER))
    #Move the bird
                if self.easy_mode == False: self.birdObj.bird_fall()


    def main(self):
        start = False
        run = True
        game_over = False
        while run:
            while not game_over:
                CLOCK.tick(FPS)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        run = False
                        game_over = True
                    if event.type == pygame.KEYDOWN:
                        start = True
                        if event.key == pygame.K_SPACE:
                            self.easy_mode = False
                            self.birdObj.jump_bird()
                        if event.key == pygame.K_UP:
                            self.easy_mode = True
                            self.birdObj.easy_mode_move("up")
                        if event.key == pygame.K_DOWN:
                            self.easy_mode = True
                            self.birdObj.easy_mode_move("down")

                    if event.type == GAME_OVER:
                        game_over = True
                if run == True: self.game_loop(start)
    #Restart game on space press
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.base = Base()
                        self.birdObj = Bird()
                        self.pipelist = []
                        self.Score = Score()
                        start = False
                        game_over = False

        pygame.quit()

game = Game()
game.main() 