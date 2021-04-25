from constants import *
class Score:

    def __init__(self):
        self.score = 0
        self.coin_count = 0
        self.start = "LET'S PLAY !!!"
        
        #self.high_score = 0
        self.font1 = pygame.font.Font("assets/04B_19.TTF", 40)
        self.font2 = pygame.font.Font("assets/04B_19.TTF", 20)
    def score_display(self,game_over, level_complete):
        if (game_over == False):
         self.score_surface = self.font1.render("SCORE: " + str(self.score),1,(255,255,255))
         self.score_rect = self.score_surface.get_rect(center= (WIDTH/2,150))
         SCREEN.blit(self.score_surface,self.score_rect)
        #display coin count
         self.coin_surface = self.font1.render("COINS: " + str(self.coin_count),1,(255,255,255))
         self.coin_rect = self.coin_surface.get_rect(center= (WIDTH/2,220))
         SCREEN.blit(self.coin_surface,self.coin_rect)
        else:
            self.score_surface = self.font1.render(f'SCORE {(self.score)}',1,(255,255,255))
            self.score_surface1 = self.font2.render(str('GAME OVER'),1,(255,255,255))
            if level_complete:
                self.score_surface1 = self.font2.render(str('LEVEL COMPLETE!'),1,(255,255,255))
            #self.score_surface2 = self.font2.render(str('PRESS SPACE TO START AGAIN'),1,(255,255,255))
            self.menu3_surface = pygame.image.load("assets/start/menu3.png").convert()
            self.score_rect = self.score_surface.get_rect(center= (WIDTH/2,200))
            self.score_rect1 = self.score_surface1.get_rect(center= (WIDTH/2,300))
            #self.score_rect2 = self.score_surface2.get_rect(center= (WIDTH/2,400))
            self.menu_rect3 = self.menu3_surface.get_rect(center= (WIDTH/2+20,400)) # (320,350)
            SCREEN.blit(self.score_surface,self.score_rect)
            SCREEN.blit(self.score_surface1,self.score_rect1)
            self.menu_display(260, 380, 120, 40, self.menu3_surface, self.menu_rect3)    
            

    def start_display(self):
        self.start_surface = self.font1.render(str(self.start), 1, (255, 255, 255))
        self.start_rect = self.start_surface.get_rect(center=(WIDTH / 2, 100))
        self.menu1_surface = pygame.image.load("assets/start/level1.png").convert()
        self.menu2_surface = pygame.image.load("assets/start/level2.png").convert()
        self.menu3_surface = pygame.image.load("assets/start/level3.png").convert()
        self.menu4_surface = pygame.image.load("assets/start/level4.png").convert()
        self.menu5_surface = pygame.image.load("assets/start/level5.png").convert()
        self.easymode_surface = pygame.image.load("assets/start/menu_1.png").convert()
        self.nmode_surface = pygame.image.load("assets/start/menu_2.png").convert()
        self.menu_rect1 = self.menu1_surface.get_rect(center= (100,270)) # (320,350)
        self.menu_rect2 = self.menu2_surface.get_rect(center= (300,270)) # (320,425)
        self.menu_rect3 = self.menu3_surface.get_rect(center= (500,270)) # (320,350)
        self.menu_rect4 = self.menu4_surface.get_rect(center= (200,370)) # (320,425)
        self.menu_rect5 = self.menu5_surface.get_rect(center= (400,370)) # (320,350)
        self.easymode_rect = self.easymode_surface.get_rect(center= (200,470)) # (320,350)
        self.nmode_rect = self.nmode_surface.get_rect(center= (400,470)) # (320,350)
        SCREEN.blit(self.start_surface, self.start_rect)
        self.menu_display(70, 240, 60, 60, self.menu1_surface, self.menu_rect1)
        self.menu_display(270, 240, 60, 60, self.menu2_surface, self.menu_rect2)
        self.menu_display(470, 240, 60, 60, self.menu3_surface, self.menu_rect3)
        self.menu_display(170, 340, 60, 60, self.menu4_surface, self.menu_rect4)
        self.menu_display(370, 340, 60, 60, self.menu5_surface, self.menu_rect5)
        self.menu_display(140, 455, 120, 30, self.easymode_surface, self.easymode_rect)
        self.menu_display(340, 455, 120, 30, self.nmode_surface, self.nmode_rect)
    def menu_display(self,X,Y,B,H,surface,surface_rect):
        self.mouse = pygame.mouse.get_pos()
        if (X+B) > self.mouse[0] > X and (Y+H) > self.mouse [1] > Y:
            surface = pygame.transform.scale(surface, (B+10,H+5))
            SCREEN.blit(surface,surface_rect)
        else:
            surface = pygame.transform.scale(surface, (B,H))
            SCREEN.blit(surface,surface_rect)
   
