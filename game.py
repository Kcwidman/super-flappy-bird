import sys
from constants import *
from bird import *
from base import *
from pipe import *
pygame.init()
pygame.display.set_caption("Flappy Bird")
base = Base()
pipeobj = Pipe()
birdobj = Bird()
GENERATE_PIPE = pygame.USEREVENT # For generating pipes
pygame.time.set_timer(GENERATE_PIPE,2000)
START = pygame.USEREVENT + 4
pygame.time.set_timer(START, 10000)
pipelist = []


def generate_pipes():
    tes=0


def game_loop():
    tes1=0


def draw_window(bird):
    SCREEN.blit(BG_SURFACE,(0,0))
    pipeobj.draw_pipe(pipelist)
    birdobj.draw_bird(bird, BIRD_BOUNDARY)
    base.draw()


def main(change, boundary):
    run = True
    while run:
        counter, text = 10, '10'.rjust(3)
        font = pygame.font.SysFont('Consolas', 30)   
        CLOCK.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == GAME_OVER:
                run = False
            """if event.type == START: 
                counter -= 1
                if counter > 0: 
                    text = str(counter)
                    print(text)
                else: 'START!'"""
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    change = birdobj.jump_bird(change)
            if event.type == GENERATE_PIPE:
                pipelist.extend(pipeobj.create_pipe())
                pipeobj.movelist(pipelist)
                

        game_loop()
        bird = birdobj.animate_bird(BIRD_SURFACE, change)
        draw_window(bird)
        pygame.display.update()
        change, boundary = birdobj.bird_fall(change, boundary)

    pygame.quit()


main(BIRD_Y_CHANGE, BIRD_BOUNDARY)