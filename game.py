import sys
import time
#local imports
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
        self.orblist = []
        self.level = None
        self.levelNum = 0;
        self.level_mode = False
        self.Score = Score()
        self.Sound = Sound()
        self.easy_mode = False
        self.game_over = False
        self.ghost_mode = False
        self.scoreMult_mode = False
        self.firePower_mode = False
        self.firePower_shot = 0

        self.start = False
        self.run = True
        self.menu = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

#helper function that calls func after a delay, can only be used in middle_loop
    def after(self, delay, func):
        start_time = time.time()
        loop = True
        while loop:
            if time.time() - start_time > delay/1000:
                func()
                loop = False
            else: self.middle_loop()
        
    def draw_window(self):
        SCREEN.blit(BG_SURFACE,(0,0))
        for pipe in self.pipelist:
                pipe.draw_pipe()
        self.base.draw()
        self.birdObj.draw_bird()
        self.Score.score_display(self.game_over)


#experimenting with orbs
        for orb in self.orblist:
                orb.draw_orb()
        pygame.display.update()

    def draw_start_window(self):
        SCREEN.blit(BG_SURFACE,(0,0))
        for pipe in self.pipelist:
            pipe.draw_pipe()
        self.base.draw()
        self.birdObj.draw_start_bird()
        self.Score.start_display()
        pygame.display.update()

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
        if self.start and not self.game_over:
            self.draw_window()
#Affect pipes
            if not self.level_mode: self.generate_pipes() #only randomly generate pipes if not in level mode
    #tally score
            for pipe in self.pipelist:
                if pipe.scorecal(self.birdObj) == True:
                    if self.scoreMult_mode == True: self.Score.score += 2
                    else: self.Score.score += 1
                    self.Sound.score_sound.play()
    #move pipes
            for pipe in self.pipelist:
                if pipe.collide(self.birdObj) == True and not self.ghost_mode:
                    self.Sound.hit.play()
                    pygame.event.post(pygame.event.Event(GAME_OVER))
                pipe.move()
    #move orbs
            for orb in self.orblist:
                if orb.collide(self.birdObj) == True:
                    self.orblist.remove(orb)
                else: orb.move()
#Check for base collision
            if self.base.collide(self.birdObj) == True:
                self.Sound.hit.play()
                pygame.event.post(pygame.event.Event(GAME_OVER))
#Move the bird
            if self.easy_mode == False: self.birdObj.bird_fall()
            self.birdObj.handle_projectile()

        elif self.game_over == False:
            self.draw_start_window()
        else:
            self.draw_window()


###################################################################################################            
    def intro_loop(self):
        CLOCK.tick(FPS)
        self.game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                self.game_over = True
            if event.type == pygame.MOUSEBUTTONDOWN and ((70+60) > event.pos[0] > 70 and (240+60) > event.pos[1] > 240):   #EASY MODE CONTROLS 
                self.start = True
                self.easy_mode = True
                self.level_mode = True
                self.levelNum = 1
            if event.type == pygame.MOUSEBUTTONDOWN and ((270+60) > event.pos[0] > 270 and (240+60) > event.pos[1] > 240):   
                self.start = True
                self.easy_mode = False 
                self.level_mode = True
                self.levelNum = 1
            if event.type == pygame.MOUSEBUTTONDOWN and ((470+60) > event.pos[0] > 470 and (240+60) > event.pos[1] > 240):   
                self.start = True
                self.easy_mode = False
                self.level_mode = True
                self.levelNum = 1
            if event.type == pygame.MOUSEBUTTONDOWN and ((170+60) > event.pos[0] > 170 and (340+60) > event.pos[1] > 340):
                self.start = True
                self.easy_mode = False
                self.level_mode = True
                self.levelNum = 1
            if event.type == pygame.MOUSEBUTTONDOWN and ((370+60) > event.pos[0] > 370 and (340+60) > event.pos[1] > 340):  
                self.start = True
                self.easy_mode = False
                self.level_mode = True
                self.levelNum = 1

        if self.level_mode:
            self.level = Level(self.levelNum)
            self.pipelist = self.level.pipes
            self.orblist = self.level.orbs

    def power_up_handling(self, event):
        if event.type == COIN_COLLISION:
            self.Score.coin_count += 1
            self.Sound.score_sound.play()
        elif event.type == FIRE_POWER:
            self.Sound.score_sound.play()
            self.firePower_start()
        elif event.type == GHOST:
            self.Sound.score_sound.play()
            self.ghost_start()
        elif event.type == SCORE_MULT:
            self.Sound.score_sound.play()
            self.scoreMult_start()

    def middle_loop(self):
        CLOCK.tick(FPS)
        self.game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                self.game_over = True
            if event.type == GAME_OVER:
                self.game_over = True
            self.power_up_handling(event)
#controls
        keys = pygame.key.get_pressed()
        if self.easy_mode:
            if keys[pygame.K_UP]: 
                self.birdObj.easy_mode_move("up")
            if keys[pygame.K_DOWN]: 
                self.birdObj.easy_mode_move("down")
            if keys[pygame.K_f]:
                self.birdObj.fire()
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
                self.level_mode = False

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

    def ghost_start(self):
        self.ghost_mode = True
        self.birdObj.change_skin("ghost")
        self.after(5000, self.ghost_end)

    def ghost_end(self):
        self.birdObj.change_skin("normal")
        self.ghost_mode = False

    def scoreMult_start(self):
        self.scoreMult_mode = True
        self.birdObj.change_skin("scoreMult")
        self.after(10000, self.scoreMult_end)

    def scoreMult_end(self):
        self.birdObj.change_skin("normal")
        self.scoreMult_mode = False

    def firePower_start(self):
        self.firePower_mode = True
        self.birdObj.change_skin("firePower")
        if self.firePower_shot > 6:
            self.firePower_end()

    def firePower_end(self):
        self.birdObj.change_skin("normal")
        self.firePower_mode = False

#executable code        
game = Game()
game.main() 
