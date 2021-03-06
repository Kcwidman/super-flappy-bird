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
from projectile import *

class Game:
    def __init__(self):
        # pygame.mixer.pre_init(frequency=44100, size=-16, channels=2, buffer= 512, devicename=None)
        pygame.init()
        pygame.display.set_caption("Flappy Bird")
        self.base = Base()
        self.birdObj = Bird()
        self.pipelist = []
        self.orblist = []
        self.level = None
        self.levelNum = 0
        self.level_mode = False
        self.Score = Score()
        self.Sound = Sound()
        self.easy_mode = False
        self.game_over = False
        self.ghost_mode = False
        self.scoreMult_mode = False
        self.firePower_mode = False
        self.firePower_shot_count = 0
        self.projectile = None
        self.level_complete = False

        self.start = False
        self.run = True
        self.test_mode = False
        self.menu = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()

#helper function that calls func after a delay, can only be used in middle_loop
#used to end powerUp effects after a certain time
    def after(self, delay, func):
        start_time = time.time()
        loop = True
        while loop and not self.game_over:
            if time.time() - start_time > delay/1000:
                func()
                loop = False
            elif not self.test_mode:
                self.middle_loop()

#calls the draw methods for all the main objects in the main middle loop
    def draw_window(self):
        if not self.test_mode:
            SCREEN.blit(BG_SURFACE,(0,0))
            #draw pipes
            for pipe in self.pipelist:
                    pipe.draw_pipe()
            self.base.draw()
            self.birdObj.draw_bird()
            self.Score.score_display(self.game_over, self.level_complete)
            #draw projectile
            if self.projectile:
                self.projectile.draw_projectile()
            #draw orbs
            for orb in self.orblist:
                    orb.draw_orb()

            pygame.display.update()

#calls the draw methods for all the main objects used in intro loop
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
    #affect pipes
            if not self.level_mode: 
                self.generate_pipes() #only randomly generate pipes if not in level mode
    #tally score
            for pipe in self.pipelist:
                if pipe.scorecal(self.birdObj) == True:
                    if self.scoreMult_mode == True: self.Score.score += 2
                    else: self.Score.score += 1
                    #self.Sound.score_sound.play()
    #move pipes
            for pipe in self.pipelist:
                if pipe.collide(self.birdObj) == True and not self.ghost_mode: #don't check for collision on ghost mode
                    #self.Sound.hit.play()
                    pygame.event.post(pygame.event.Event(GAME_OVER))
                pipe.move()
    #move orbs
            for orb in self.orblist:
                if orb.collide(self.birdObj) == True: #remove orbs if collision
                    self.orblist.remove(orb)
                else: orb.move()
    #Check for base collision
            if self.base.collide(self.birdObj) == True:
                #self.Sound.hit.play()
                pygame.event.post(pygame.event.Event(GAME_OVER))#end game 
    #Move the bird
            if self.easy_mode == False: self.birdObj.bird_fall() #move the bird if easy mode not activated
    #Handle projectile
            if self.projectile:
                self.projectile.move_projectile()
                for pipe in self.pipelist:
                    if self.projectile:#need to make sure that the loop doesn't continue after the first collison
                        if pipe.collide(self.projectile):#remove the projectile and decrement health
                            pipe.health -= 1
                            self.projectile = None
                        if pipe.health == 0:#remove pipe if health drops to 0
                            self.pipelist.remove(pipe)
    #check if the last pipe reaches end to complete the level or if pipelist is empty
            if not self.pipelist or (self.level_mode and (self.pipelist[-1].x_loc + PIPE_WIDTH < 0)):
                pygame.event.post(pygame.event.Event(LEVEL_COMPLETE))
    #these last 2 statements handle cases for intro and end loops (explained down below)
        elif self.game_over == False:
            self.draw_start_window()
        else:
            self.draw_window()


###################################################################################################     
#intro loop is run before the user selects an option from the menu       
    def intro_loop(self):
        CLOCK.tick(FPS)
        self.game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                self.game_over = True
        #select menu items
            if event.type == pygame.MOUSEBUTTONDOWN and ((140+120) > event.pos[0] > 140 and (455+30) > event.pos[1] > 455):   #EASY MODE
                self.start = True
                self.easy_mode = True
                self.level_mode = False
            if event.type == pygame.MOUSEBUTTONDOWN and ((340+120) > event.pos[0] > 340 and (455+30) > event.pos[1] > 455):   #NORMAL MODE
                self.start = True
                self.easy_mode = False
                self.level_mode = False
            if event.type == pygame.MOUSEBUTTONDOWN and ((70+60) > event.pos[0] > 70 and (240+60) > event.pos[1] > 240):   #LEVEL 1
                self.start = True
                self.easy_mode = False
                self.level_mode = True
                self.levelNum = 1
            if event.type == pygame.MOUSEBUTTONDOWN and ((270+60) > event.pos[0] > 270 and (240+60) > event.pos[1] > 240):    #LEVEL 2
                self.start = True
                self.easy_mode = False
                self.level_mode = True
                self.levelNum = 2
            if event.type == pygame.MOUSEBUTTONDOWN and ((470+60) > event.pos[0] > 470 and (240+60) > event.pos[1] > 240):    #LEVEL 3
                self.start = True
                self.easy_mode = False
                self.level_mode = True
                self.levelNum = 3
            if event.type == pygame.MOUSEBUTTONDOWN and ((170+60) > event.pos[0] > 170 and (340+60) > event.pos[1] > 340):   #LEVEL 4
                self.start = True
                self.easy_mode = False
                self.level_mode = True
                self.levelNum = 4
            if event.type == pygame.MOUSEBUTTONDOWN and ((370+60) > event.pos[0] > 370 and (340+60) > event.pos[1] > 340):   #LEVEL 5
                self.start = True
                self.easy_mode = False
                self.level_mode = True
                self.levelNum = 5
        #load the level objects if level mode selected
        if self.level_mode:
            self.level = Level(self.levelNum)
            self.pipelist = self.level.pipes
            self.orblist = self.level.orbs

#calls the proper functions when a power up collision occurs
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
#middle loop runs the main game loop and is used for actual gameplay
    def middle_loop(self):
        if not self.test_mode: CLOCK.tick(FPS)#this dramatically speeds up tests
        self.game_loop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                self.game_over = True
            if event.type == GAME_OVER:
                self.game_over = True
#check for level complete
            if event.type == LEVEL_COMPLETE:
                self.game_over = True
                self.level_complete = True
            self.power_up_handling(event)
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
    #turn to easy mode if 'e' is pressed
        if keys[pygame.K_e]:
            self.easy_mode = True
        if keys[pygame.K_f] and self.firePower_mode and not self.projectile:
            self.fire()

        if self.game_over: self.game_loop()
    
#shown after game over event occurs and runs until the game is quit or restarted
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
                self.level_complete = False
                self.ghost_mode = False
                self.scoreMult_mode = False
                self.firePower_mode = False
                self.firePower_shot_count = 0
                self.projectile = None

    def main(self):
        pygame.mixer.music.play(-1)
        while self.run:
            if not self.game_over and not self.start: #run before the game starts
                self.intro_loop()
            elif not self.game_over and self.start: #run while the game is being played
                self.middle_loop()
            else:                                   #run after the game ends but before the next game begins
                self.end_loop()
                        
            pygame.QUIT

#used in the test suite, it will advance the game loop as many frames as taken in as a parameter
#this allows for very accurate testing
    def test_main(self, frames):
        self.test_mode = True
        self.start = True
        count = 0
        while count <= frames - 1:#will step throught the game loop for as many frames as specified
            if not self.game_over:
                self.middle_loop()
                count += 1
            else:
                break

    def end_testing(self):
        pygame.quit()

#POWER UP FUNCTIONS
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

    def firePower_end(self):
        self.birdObj.change_skin("normal")
        self.firePower_mode = False

    def fire(self):
        self.projectile = Projectile(self.birdObj.x_loc, self.birdObj.y_loc)
        self.firePower_shot_count += 1
        if self.firePower_shot_count >= 4:
            self.firePower_end()