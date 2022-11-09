from pico2d import *
import game_world
import game_framework


PIXEL_PER_METER=10.0/0.3
RUN_SPEED_KPH=20.0
RUN_SPEED_MPM=RUN_SPEED_KPH*1000.0/60
RUN_SPEED_MPS=RUN_SPEED_MPM/60.0
RUN_SPEED_PPS=RUN_SPEED_MPS *PIXEL_PER_METER


class BIRD:
    image = None

    def __init__(self, x = 400, y = 300, dir=1):
        if BIRD.image == None:
            BIRD.image = load_image('bird_animation.png')
        self.x, self.y, self.dir = x, y, dir
        self.framex=0
        self.framey=0
    def draw(self):
        if self.dir>0:
            self.image.clip_draw(self.framex * 186, self.framey, 186, 167, self.x, self.y, 50, 50)
        else:
            self.image.clip_composite_draw(self.framex * 186, self.framey, 186, 167, 0, 'h', self.x, self.y, 50, 50)

    def update(self):
        self.x += self.dir*RUN_SPEED_PPS*game_framework.frame_time
        self.framex =(self.framex+1)%5
        if self.x < 25 or self.x >800 - 25:
            if self.x<25:
                self.dir=1
            elif self.x >800 - 25 :
                self.dir=-1

