from constants import *

class Bird:
    birdDown = pygame.image.load('assets/bird3.png').convert_alpha()
    birdCenter = pygame.image.load('assets/bird2.png').convert_alpha()
    birdUp = pygame.image.load('assets/bird1.png').convert_alpha()
    birdFrame = [birdDown, birdCenter, birdUp]
    tick_count = 0
    falling_vel = 0
    rot_angle = 0
    frame_index = 0
    bird_img = birdFrame[0]
    y_loc = BIRD_START_Y_LOC
    x_loc = BIRD_START_X_LOC
    boundary = BIRD_SURFACE.get_rect(topleft = (x_loc, y_loc))

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