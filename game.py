import sys
from constants import *
from bird import *
from base import *
from pipe import *
from score import *
pygame.init()
pygame.display.set_caption("Flappy Bird")
base = Base()
birdObj = Bird()
pipelist = []
Score = Score()

def draw_window():
    SCREEN.blit(BG_SURFACE,(0,0))
    for pipe in pipelist:
        pipe.draw_pipe()
    birdObj.draw_bird()
    Score.score_display()
    base.draw()


def generate_pipes():
#GENERATE PIPES
    if len(pipelist) == 0:
        for i in range (1, 5):#(1,5)
            pipelist.append(Pipe(WIDTH + i*PIPE_SPACING))#WIDTH + i*PIPE_SPACING
#DELETE PIPES WHEN THEY GO OFF SCREEN
    if pipelist[0].x_loc <= -PIPE_WIDTH:
        pipelist.append(Pipe(WIDTH + PIPE_SPACING + pipelist[0].x_loc))
        pipelist.pop(0)
    
    
def game_loop(start):
    draw_window()
    pygame.display.update()
    if start:
#Affect pipes
            generate_pipes()
            for pipe in pipelist:
                if pipe.scorecal(birdObj) == True:
                    Score.score += 1
            for pipe in pipelist:
                if pipe.collide(birdObj) == True:
                    pygame.event.post(pygame.event.Event(GAME_OVER))
                pipe.move()
                
#Check for base collision
            if base.collide(birdObj) == True:
                pygame.event.post(pygame.event.Event(GAME_OVER))
#Move the bird
            
            birdObj.bird_fall()
            



def main():
    start = False
    run = True
    while run:
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == GAME_OVER: 
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    start = True
                    birdObj.jump_bird()
        if run == True: game_loop(start)

    pygame.quit()


main()