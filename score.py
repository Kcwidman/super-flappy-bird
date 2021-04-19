from constants import *
class Score:

    def __init__(self):
        self.score = 0
        self.start = "LET'S PLAY !!!"
        
        #self.high_score = 0
        self.font1 = pygame.font.Font("assets/04B_19.TTF", 40)
        self.font2 = pygame.font.Font("assets/04B_19.TTF", 20)
    def score_display(self,game_over):
        if (game_over == False):
         self.score_surface = self.font1.render(str(self.score),1,(255,255,255))
         self.score_rect = self.score_surface.get_rect(center= (WIDTH/2,200))
         SCREEN.blit(self.score_surface,self.score_rect)
        else:
            self.score_surface = self.font1.render(f'SCORE {(self.score)}',1,(255,255,255))
            self.score_surface1 = self.font2.render(str('GAME OVER'),1,(255,255,255))
            #self.score_surface2 = self.font2.render(str('PRESS SPACE TO START AGAIN'),1,(255,255,255))
            self.menu3_surface = pygame.image.load("assets/menu3.png").convert()
            self.score_rect = self.score_surface.get_rect(center= (WIDTH/2,200))
            self.score_rect1 = self.score_surface1.get_rect(center= (WIDTH/2,300))
            #self.score_rect2 = self.score_surface2.get_rect(center= (WIDTH/2,400))
            self.menu_rect3 = self.menu3_surface.get_rect(center= (WIDTH/2+20,400)) # (320,350)
            SCREEN.blit(self.score_surface,self.score_rect)
            SCREEN.blit(self.score_surface1,self.score_rect1)
            self.menu_display(260, 380, 120, 40, self.menu3_surface, self.menu_rect3)    
            print('yes')
            

    def start_display(self):
        self.start_surface = self.font1.render(str(self.start), 1, (255, 255, 255))
        self.start_rect = self.start_surface.get_rect(center=(WIDTH / 2, 200))
        self.menu1_surface = pygame.image.load("assets/menu1.png").convert()
        self.menu2_surface = pygame.image.load("assets/menu2.png").convert()
        self.menu_rect1 = self.menu1_surface.get_rect(center= (WIDTH/2+20,350)) # (320,350)
        self.menu_rect2 = self.menu2_surface.get_rect(center= (WIDTH/2+20,425)) # (320,425)
        SCREEN.blit(self.start_surface, self.start_rect)
        self.menu_display(260, 320, 120, 40, self.menu1_surface, self.menu_rect1)
        self.menu_display(260, 395, 120, 45, self.menu2_surface, self.menu_rect2)

    def menu_display(self,X,Y,B,H,surface,surface_rect):
        self.mouse = pygame.mouse.get_pos()
        if (X+B) > self.mouse[0] > X and (Y+H) > self.mouse [1] > Y:
            surface = pygame.transform.scale(surface, (B+10,H+5))
            SCREEN.blit(surface,surface_rect)
        else:
            surface = pygame.transform.scale(surface, (B,H))
            SCREEN.blit(surface,surface_rect)
   
