import pyglet
import random
from config import *

from ctypes import *
import time

windll.user32.BlockInput(1)


window = pyglet.window.Window(fullscreen = True)
window.set_exclusive_mouse(True)
window.set_exclusive_keyboard(True)
pyglet.gl.glClearColor(0,0,1,1)

text_count = 1

display_text = pyglet.text.Label('',
                                 font_name = 'terminal',
                                 font_size = 26,
                                 x = 10,
                                 y = window.height - 10,
                                 width = window.width - 10,
                                 anchor_x = 'left',
                                 anchor_y = 'top',
                                 multiline=True)


def update(dt):
    global text
    global text_count
    display_text.text = text + pop_text.format(int(text_count))
    text_count += random.random()*dt*2.5
    if text_count - int(text_count) < 0.02:
        display_text.text = text

@window.event
def on_draw():
    window.clear()
    display_text.draw()


pyglet.clock.schedule_interval(update, 1/60)


pyglet.app.run()
