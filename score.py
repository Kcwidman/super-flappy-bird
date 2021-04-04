from constants import *
class Score:

    def __init__(self):
        self.score = 0 
        #self.high_score = 0
        #self.font1 = pygame.font.Font("C:\Windows\Fonts\Arial.ttf",40)
        self.font1 = pygame.font.Font("assets/04B_19.TTF", 40)

        
    def score_display(self):
        outlineSurf = self.font1.render(str(self.score), True, (0, 0, 0))
        self.score_surface = self.font1.render(str(self.score),1,(255,255,255))
        self.score_rect = self.score_surface.get_rect(center= (WIDTH/2,200))
        SCREEN.blit(self.score_surface,self.score_rect)


