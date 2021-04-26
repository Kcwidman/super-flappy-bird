from constants import *

class Base:
    x_loc = 0
    y_loc = FLOOR

    #scrolling bar at the bottom of the page
    def draw(self):
        self.x_loc -= VEL
        SCREEN.blit(BASE_SURFACE,(self.x_loc, self.y_loc))
        SCREEN.blit(BASE_SURFACE,(self.x_loc + WIDTH, self.y_loc))
        if self.x_loc <= -WIDTH:
            self.x_loc = 0

    #checks for collision with base
    def collide(self, bird):
        if bird.y_loc + bird.bird_img.get_height() + 9 >= self.y_loc:
            return True
        else:
            return False