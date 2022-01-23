import ctypes
'''
from pynput.keyboard import Key,Controller,Listener
'''
ctypes.windll.user32.BlockInput(1)
'''
keyboard = Controller()

def on_press(key):
    if key == Key.shift:
        return False 
def on_release(key):
    pass


with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()

ctypes.windll.user32.BlockInput(0)
'''
while True:
    pass
