import pico2d
import play_station
import logo_state
state = logo_state


pico2d.open_canvas()
state.enter()



# game main loop code
states=[logo_state,play_station]
for state in states:
    state.enter()
    while state.running:
        state.handle_events()
        state.update()
        state.draw()
state.exit()

# finalization code
pico2d.close_canvas()



