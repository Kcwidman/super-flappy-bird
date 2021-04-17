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
            self.score_surface2 = self.font2.render(str('PRESS SPACE TO START AGAIN'),1,(255,255,255))
            self.score_rect = self.score_surface.get_rect(center= (WIDTH/2,200))
            self.score_rect1 = self.score_surface1.get_rect(center= (WIDTH/2,300))
            self.score_rect2 = self.score_surface2.get_rect(center= (WIDTH/2,400))
            SCREEN.blit(self.score_surface,self.score_rect)
            SCREEN.blit(self.score_surface1,self.score_rect1)
            SCREEN.blit(self.score_surface2,self.score_rect2)           
            

    def start_display(self):
        self.mouse = pygame.mouse.get_pos()
        self.start_surface = self.font1.render(str(self.start), 1, (255, 255, 255))
        self.start_rect = self.start_surface.get_rect(center=(WIDTH / 2, 200))
        SCREEN.blit(self.start_surface, self.start_rect)
        if (260+120) > self.mouse[0] > 260 and (320+60) > self.mouse [1] > 320:
            self.menu1_surface = pygame.image.load("assets/menu1.png").convert()
            self.menu1_surface = pygame.transform.scale(self.menu1_surface, (120,45))
            self.menu_rect1 = self.menu1_surface.get_rect(center= (WIDTH/2+20,350))
            SCREEN.blit(self.menu1_surface,self.menu_rect1)
        else:
            self.menu1_surface = pygame.image.load("assets/menu1.png").convert()
            self.menu1_surface = pygame.transform.scale(self.menu1_surface, (130,50))
            self.menu_rect1 = self.menu1_surface.get_rect(center= (WIDTH/2+20,350))
            SCREEN.blit(self.menu1_surface,self.menu_rect1)

        if (260+120) > self.mouse[0] > 260 and (395+60) > self.mouse [1] > 395:
            self.menu2_surface = pygame.image.load("assets/menu2.png").convert()
            self.menu2_surface = pygame.transform.scale(self.menu2_surface, (120,60))
            self.menu_rect2 = self.menu2_surface.get_rect(center= (WIDTH/2+20,425))
            SCREEN.blit(self.menu2_surface,self.menu_rect2)
        else:
            self.menu2_surface = pygame.image.load("assets/menu2.png").convert()
            self.menu2_surface = pygame.transform.scale(self.menu2_surface, (130,65))
            self.menu_rect2 = self.menu2_surface.get_rect(center= (WIDTH/2+20,425))
            SCREEN.blit(self.menu2_surface,self.menu_rect2)


   
