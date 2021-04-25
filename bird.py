from constants import *

class Bird:
    birdDown = pygame.image.load('assets/bird_down.png').convert_alpha()
    birdCenter = pygame.image.load('assets/bird_mid.png').convert_alpha()
    birdUp = pygame.image.load('assets/bird_up.png').convert_alpha()
    birdFrame = [birdDown, birdCenter, birdUp]
    tick_count = 0
    falling_vel = 0
    rot_angle = 0
    frame_index = 0
    frame_index1 = 0
    bird_img = birdFrame[0]
    y_loc = BIRD_START_Y_LOC
    x_loc = BIRD_START_X_LOC
    boundary = BIRD_SURFACE.get_rect(topleft = (x_loc, y_loc))
    power_mode = ""

    #####################################################################################################################################
    birdDown1 = pygame.image.load('assets/start/fire_down.png').convert_alpha()
    birdCenter1 = pygame.image.load('assets/start/fire_mid.png').convert_alpha()
    birdUp1 = pygame.image.load('assets/start/fire_up.png').convert_alpha()
    birdDown2 = pygame.image.load('assets/start/mult_down.png').convert_alpha()
    birdCenter2 = pygame.image.load('assets/start/mult_mid.png').convert_alpha()
    birdUp2 = pygame.image.load('assets/start/mult_up.png').convert_alpha()
    birdDown3 = pygame.image.load('assets/start/red_down.png').convert_alpha()
    birdCenter3 = pygame.image.load('assets/start/red_mid.png').convert_alpha()
    birdUp3 = pygame.image.load('assets/start/red_up.png').convert_alpha()
    birdDown4 = pygame.image.load('assets/start/ghost_down.png').convert_alpha()
    birdCenter4 = pygame.image.load('assets/start/ghost_mid.png').convert_alpha()
    birdUp4 = pygame.image.load('assets/start/ghost_up.png').convert_alpha()
    birdFrame1 = [birdDown, birdCenter, birdUp,birdDown1, birdCenter1, birdUp1,birdDown2, birdCenter2, birdUp2,birdDown3, birdCenter3, birdUp3, birdDown4, birdCenter4, birdUp4]
    bird_img2 = birdFrame1[0]

    def animate_start_bird(self):
	    self.tick_count += 1
	    if self.tick_count % 15 == 0:
	        self.frame_index1 = (self.frame_index1 + 1) % 15
	    self.bird_img2 = pygame.transform.rotozoom(self.birdFrame1[self.frame_index1], max(-self.falling_vel * 5, -70), 1)

    def draw_start_bird(self):
        self.animate_start_bird()
        SCREEN.blit(self.bird_img2,(WIDTH/2-20,HEIGHT/2-100))

    #######################################################################################################################################

    def change_skin(self, power):
        self.power_mode = power #allow game to see what mode the bird is in
        if power == "normal":
            self.birdDown = pygame.image.load('assets/bird_down.png').convert_alpha()
            self.birdCenter = pygame.image.load('assets/bird_mid.png').convert_alpha()
            self.birdUp = pygame.image.load('assets/bird_up.png').convert_alpha()
            self.birdFrame = [self.birdDown, self.birdCenter, self.birdUp]

        if power == "ghost":
            self.birdDown = pygame.image.load('assets/powerUps/ghost_down.png').convert_alpha()
            self.birdCenter = pygame.image.load('assets/powerUps/ghost_mid.png').convert_alpha()
            self.birdUp = pygame.image.load('assets/powerUps/ghost_up.png').convert_alpha()
            self.birdFrame = [self.birdDown, self.birdCenter, self.birdUp]

        if power == "firePower":
            self.birdDown = pygame.image.load('assets/powerUps/fire_down.png').convert_alpha()
            self.birdCenter = pygame.image.load('assets/powerUps/fire_mid.png').convert_alpha()
            self.birdUp = pygame.image.load('assets/powerUps/fire_up.png').convert_alpha()
            self.birdFrame = [self.birdDown, self.birdCenter, self.birdUp]

        if power == "scoreMult":
            self.birdDown = pygame.image.load('assets/powerUps/mult_down.png').convert_alpha()
            self.birdCenter = pygame.image.load('assets/powerUps/mult_mid.png').convert_alpha()
            self.birdUp = pygame.image.load('assets/powerUps/mult_up.png').convert_alpha()
            self.birdFrame = [self.birdDown, self.birdCenter, self.birdUp]

    def animate_bird(self):
        self.tick_count += 1
        if self.tick_count % 3 == 0:
            self.frame_index = (self.frame_index + 1) % 3
        self.bird_img = pygame.transform.rotozoom(self.birdFrame[self.frame_index], max(-self.falling_vel * 5, -70), 1)

    def draw_bird(self):
        self.animate_bird()
        SCREEN.blit(self.bird_img, self.boundary)

    def bird_fall(self):
        self.rot_angle = -self.falling_vel * 5
        self.falling_vel += FALLING_ACC
        if self.falling_vel > TERMINAL_VEL: self.falling_vel = TERMINAL_VEL
        self.y_loc += self.falling_vel
        self.boundary = BIRD_SURFACE.get_rect(topleft = (self.x_loc, self.y_loc))
        self.in_bounds_check()

    def jump_bird(self):
        self.falling_vel = JUMP_HEIGHT

    def get_mask(self):
        return pygame.mask.from_surface(self.bird_img)

    def easy_mode_move(self, direction):
        self.falling_vel = 0
        if direction == "up":
            self.y_loc -= 7
        if direction == "down":
            self.y_loc += 7
        self.boundary = BIRD_SURFACE.get_rect(topleft = (self.x_loc, self.y_loc))
        self.in_bounds_check()
    
    def in_bounds_check(self):
        if self.y_loc < 0:
            self.y_loc = 0
            self.boundary = BIRD_SURFACE.get_rect(topleft = (self.x_loc, self.y_loc))
    