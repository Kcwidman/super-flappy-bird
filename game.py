import sys
from constants import *
from bird import *
from base import *
from pipe import *
from score import *
from sound import *
from level import *
class Game:
    def __init__(self):
        #pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer= 512, devicename=None)
        pygame.init()
        pygame.display.set_caption("Flappy Bird")
        self.base = Base()
        self.birdObj = Bird()
        self.pipelist = []
        self.level = Level(1)
        self.Score = Score()
        self.Sound = Sound()
        self.easy_mode = False
        self.game_over = False
        self.level_mode = False
        self.level_init = True
        self.start = False
        self.run = True
        self.menu = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        
    def draw_window(self,game_over):
        if game_over== False:
            SCREEN.blit(BG_SURFACE,(0,0))
            for pipe in self.pipelist:
                pipe.draw_pipe()
            self.base.draw()
            self.birdObj.draw_bird()
            self.Score.score_display(self.game_over)
        else:
            SCREEN.blit(BG_SURFACE,(0,0))
            for pipe in self.pipelist:
                pipe.draw_pipe()
            self.base.draw()
            self.birdObj.draw_bird()
            self.Score.score_display(self.game_over)
            self.Score.score_display(self.game_over)


#experimenting with orbs
        # if self.level.orbs:
        #     self.level.orbs[0].move()
        #     self.level.orbs[0].draw_orb()
        #     if self.level.orbs[0].collide(self.birdObj):
        #         self.level.orbs.pop(0)

    def draw_start_window(self):
        SCREEN.blit(BG_SURFACE,(0,0))
        for pipe in self.pipelist:
            pipe.draw_pipe()
        self.base.draw()
        self.birdObj.draw_bird()
        self.Score.start_display()

    def generate_pipes(self):
    #GENERATE PIPES
        if len(self.pipelist) == 0:
            for i in range (1, 5):#(1,5)
                self.pipelist.append(Pipe(WIDTH + i*PIPE_SPACING, 0))#WIDTH + i*PIPE_SPACING
    #DELETE PIPES WHEN THEY GO OFF SCREEN
        if self.pipelist[0].x_loc <= -PIPE_WIDTH:
            self.pipelist.append(Pipe(WIDTH + PIPE_SPACING + self.pipelist[0].x_loc, 0))
            self.pipelist.pop(0)
        
        
    def game_loop(self):
        #self.draw_window()
        #pygame.display.update()
        if self.start and not self.game_over:
                self.draw_window(self.game_over)
                pygame.display.update()
    #Affect pipes
                if not self.level_mode: self.generate_pipes() #only randomly generate pipes if not in level mode
        #tally score
                for pipe in self.pipelist:
                    if pipe.scorecal(self.birdObj) == True:
                        self.Score.score += 1
                        self.Sound.score_sound.play()
        #move pipes
                for pipe in self.pipelist:
                    if pipe.collide(self.birdObj) == True:
                        self.Sound.hit.play()
                        pygame.event.post(pygame.event.Event(GAME_OVER))
                    pipe.move()
    #Check for base collision
                if self.base.collide(self.birdObj) == True:
                    self.Sound.hit.play()
                    pygame.event.post(pygame.event.Event(GAME_OVER))
    #Move the bird
                if self.easy_mode == False: self.birdObj.bird_fall()
        elif self.game_over == False:
            self.draw_start_window()
            pygame.display.update()
        else:
            self.draw_window(self.game_over)
            pygame.display.update()


###################################################################################################            
    def intro_loop(self):
        CLOCK.tick(FPS)
        self.game_loop()
        if self.level_mode:
            if self.level_init:
                self.pipelist = self.level.pipes;
                self.level_init = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                self.game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN and ((260+120) > event.pos[0] > 260 and (320+40) > event.pos[1] > 320):
                self.start = True
                self.easy_mode = False   
            if event.type == pygame.MOUSEBUTTONDOWN and ((260+120) > event.pos[0] > 260 and (395+45) > event.pos[1] > 395):   #EASY MODE CONTROLS 
                self.start = True
                self.easy_mode = True
                # self.level_mode = True

    def middle_loop(self):
        CLOCK.tick(FPS)
        self.game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                self.game_over = True
            if event.type == GAME_OVER:
                self.game_over = True
#controls
        keys = pygame.key.get_pressed()
        if self.easy_mode:
            if keys[pygame.K_UP]: 
                self.birdObj.easy_mode_move("up")
            if keys[pygame.K_DOWN]: 
                self.birdObj.easy_mode_move("down")
        else:
            if keys[pygame.K_SPACE]: 
                self.birdObj.jump_bird()

        if self.game_over: self.game_loop()
    
    def end_loop(self):
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                self.game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN and ((260+120) > event.pos[0] > 260 and (380+40) > event.pos[1] > 380):
                self.base = Base()
                self.birdObj = Bird()
                self.pipelist = []
                self.Score = Score()
                self.start = False
                self.game_over = False
                self.level_init = True

    def main(self):
        pygame.mixer.music.play(-1)
        while self.run:
            if not self.game_over and not self.start: #run before the game starts
                self.intro_loop()
            elif not self.game_over and self.start: #run while the game is being played
                self.middle_loop()
            else:                                   #run after the game ends but before the next game begins
                self.end_loop()
                        
        pygame.quit()

#executable code        
game = Game()
game.main() 
