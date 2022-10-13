
from pico2d import *
import game_framework
import logo_state
import item_state
import delete_state

class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)

class Boy:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('animation_sheet.png')
        self.dir=1
        self.ball_image = load_image('ball21x21.png')
        self.big_ball_image=load_image('ball41x41.png')
        self.item='BigBall'

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir*2
        if(self.x>800):
            self.dir=-1
            self.x=800
        elif(self.x<0):
            self.x=0
            self.dir=1

    def draw(self):
        if self.dir==1:
            self.image.clip_draw(self.frame * 100, 100, 100, 100, self.x, self.y)

        elif self.dir==-1:
            self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

        if self.item =='BigBall':
            self.big_ball_image.draw(self.x+10,self.y+50)
        elif self.item =='Ball':
            self.ball_image.draw(self.x+10,self.y+50)
    def add(self ):
        {

        }


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.change_state(logo_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_i:
            game_framework.push_state(item_state)
        elif event.type == SDL_KEYDOWN and event.key == SDLK_b:
            game_framework.push_state(delete_state)

open_canvas()

def make_char():
    global teams,boy
    teams.append(Boy())

def enter():
   global boy,grass, running
   boy=Boy()
   grass=Grass()





teams=[Boy()]
boy = Boy()
grass = Grass()
running = True

#game end code- 객체를 소멸
def exit():
    global boy, grass
    del boy
    del grass
    pass

def update():
    boy.update()
    for boys in teams:
        boys.update()

def draw_world():
    grass.draw()
    boy.draw()
    for boys in teams:
        boys.draw()

def draw():
    # game wolrd rendering
    clear_canvas()
    grass.draw()
    boy.draw()
    for boys in teams:
        boys.draw()
    update_canvas()

def pause():
    pass

def resume():
    pass


def test_self():
    import sys
    this_module= sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()

if __name__=='__main__':
    test_self()



