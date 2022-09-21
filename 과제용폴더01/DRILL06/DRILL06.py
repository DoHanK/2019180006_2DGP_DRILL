from pico2d import *
from math import*
open_canvas()

# fill here
grass=load_image('grass.png')
character=load_image('character.png')

x=0
y=90
while(True):
    x=0
    y=90
    while(x<800):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x+=2
    while(y<600):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y+=2
    while(x>0):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x-=2
    while(y>90):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        y-=2
    x=300
    y=90
    angle=0
    limit=0
    while(limit<1000):
        clear_canvas_now()
        grass.draw_now(400,30)
        character.draw_now(x,y)
        x+=4*math.cos(angle/360*2*math.pi)
        y+=4*math.sin(angle/360*2*math.pi)
        angle+=1
        limit+=1
   
close_canvas()
