import pico2d
from pico2d import *

import game_framework
import play_station


image = None

def enter():
    global image
    image = load_image("add_delete_boy.png")
    pass

def exit():
    # fill here
    pass

def handle_events():
    global events
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.pop_state()
                case pico2d.SDLK_0:
                    play_station.boy.item = None
                    game_framework.pop_state()
                case pico2d.SDLK_1:
                    play_station.boy.item ='Ball'
                    game_framework.pop_state()
                case pico2d.SDLK_2:
                    play_station.boy.item ='BigBall'
                    game_framework.pop_state()



    pass

def draw():
    clear_canvas()
    play_station.draw_world()
    image.draw(400,300)
    update_canvas()

def update():
    pass

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





