from constants import *
class Score:

    def __init__(self):
        self.score = 0
        self.start = "PRESS SPACE TO START"
        #self.high_score = 0
        #self.font1 = pygame.font.Font('04B_19.TTF',40)
        #self.font1 = pygame.font.Font("C:\Windows\Fonts\Arial.ttf",40)
        self.font1 = pygame.font.Font("assets/04B_19.TTF", 40)

        
    def score_display(self,game_over):
        if (game_over == False):
         #outlineSurf = self.font1.render(str(self.score), True, (0, 0, 0))
         self.score_surface = self.font1.render(str(self.score),1,(255,255,255))
         self.score_rect = self.score_surface.get_rect(center= (WIDTH/2,200))
         SCREEN.blit(self.score_surface,self.score_rect)
        else:
            #print('game over')
            self.score_surface = self.font1.render(str(self.score),1,(255,255,255))
            self.score_surface1 = self.font1.render(str('GAME OVER'),1,(255,255,255))
            self.score_surface2 = self.font1.render(str('PRESS SPACE TO START AGAIN'),1,(255,255,255))
            self.score_rect = self.score_surface.get_rect(center= (WIDTH/2,200))
            self.score_rect1 = self.score_surface1.get_rect(center= (WIDTH/2,300))
            self.score_rect2 = self.score_surface2.get_rect(center= (WIDTH/2,400))
            SCREEN.blit(self.score_surface,self.score_rect)
            SCREEN.blit(self.score_surface1,self.score_rect1)
            SCREEN.blit(self.score_surface2,self.score_rect2)

    def start_display(self):
        self.start_surface = self.font1.render(str(self.start), 1, (255, 255, 255))
        self.start_rect = self.start_surface.get_rect(center=(WIDTH / 2, 200))
        SCREEN.blit(self.start_surface, self.start_rect)