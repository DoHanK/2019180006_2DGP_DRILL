
from pico2d import *
open_canvas()
character =load_image("cutpic1.png")
x=400
frame=0
y=300
def walk(frame,x):
    clear_canvas()
    character.clip_draw(frame*120+10,0,120,100,x,y)
    update_canvas()

    delay(0.1)




while(x<500):
    walk(frame,x)
    frame = (frame + 1) % 4
    x += 5
    delay(0.1)
    get_events()

character =load_image("cutpic2.png")
while(x<700):
    walk(frame,x)
    frame = (frame + 1) % 4
    x += 5
    y-=5
    delay(0.1)
    get_events()
character =load_image("cutpic3.png")
while(y>50):
    walk(frame,x)
    frame = (frame + 1) % 4
    y-=5
    delay(0.1)
    get_events()


get_events()

close_canvas()

