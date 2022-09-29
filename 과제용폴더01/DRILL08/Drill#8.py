from pico2d import *


KPU_WIDTH, KPU_HEIGHT = 800, 600

def handle_events():
    global running
    global dirx,framey,diry

    events=get_events()
    for event in events:
        if event.type ==SDL_QUIT:
            running =False
        elif event.type ==SDL_KEYDOWN:
            if event.key==SDLK_RIGHT:
                dirx+=1
                framey=1
            elif event.key==SDLK_LEFT:
                dirx-=1
                framey =0
            if event.key==SDLK_DOWN:
                diry-=1
                if framey==1:
                    framey=3
                elif framey==0:
                    framey=2

            elif event.key==SDLK_UP:
                diry+=1
                if framey==1:
                    framey=3
                elif framey==0:
                    framey=2

            elif event.key==SDLK_ESCAPE:
                running =False
        elif event.type==SDL_KEYUP:
            if event.key==SDLK_RIGHT:
                dirx-=1
                framey=1
            elif event.key==SDLK_LEFT:
                dirx+=1
                framey =0
            if event.key==SDLK_DOWN:
                diry+=1
                if framey==1:
                    framey=3
                elif framey==0:
                    framey=2

            elif event.key==SDLK_UP:
                diry-=1
                if framey==1:
                    framey=3
                elif framey==0:
                    framey=2

    pass


open_canvas(KPU_WIDTH,KPU_HEIGHT)
grass = load_image('TUK_GROUND.png')
character = load_image('animation_sheet.png')

running = True
x = 800 // 2
y= 800 // 2
framex = 0
framey = 0
dirx=0
diry=0

while running:
    clear_canvas()
    grass.draw(KPU_WIDTH // 2, KPU_HEIGHT // 2)
    character.clip_draw(framex * 100, 100 * framey, 100, 100, x, y)
    update_canvas()

    handle_events()
    framex = (framex + 1) % 8

    x+=dirx*5
    if x<10:
     x+=5
    elif x>KPU_WIDTH-10:
        x-=5

    y+=diry*5
    if y < 0+20:
        y += 5
    elif y > KPU_HEIGHT-20:
        y -= 5
    delay(0.01)

close_canvas()