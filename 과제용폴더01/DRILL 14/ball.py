from pico2d import *

import game_world
import server

class Ball:
    image=None
    def __init__(self, x, y):
        if Ball.image==None:
            Ball.image=load_image("ball21x21.png")


        self.x=x
        self.y=y
        self.frame_x=0
        self.frame_y=0

    def get_bb(self):
        sx = server.background.window_left
        sy = server.background.window_bottom
        return self.x - 10-sx ,self.y - 10 - sy, self.x + 10-sx ,self.y + 10-sy
        pass
    def update(self):
        self.frame_x= (int)(self.frame_x +1) %4

    def draw(self):
        sx=server.background.window_left
        sy=server.background.window_bottom
        self.image.clip_draw(0,  0, 100,  100, self.x-sx, self.y-sy,  20,  20)
        draw_rectangle(*self.get_bb())

    def handle_collision(self,other,massage):
        game_world.remove_object(self)
        pass