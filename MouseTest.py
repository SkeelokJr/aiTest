# first open terminal and type "pip install pyautogui" and "pip install keyboard"

import pyautogui as pag
import keyboard as kb

running = True

screen_size = pag.size()
screen_width, screen_height = screen_size[0], screen_size[1]
screen_centerX, screen_centerY = screen_width/2, screen_height/2

def start():
    pag.moveTo(screen_centerX, screen_centerY)
    pag.click(button='left')
    pag.write("testing")
    pag.click(button='left')
    pag.click(button='left')
    while True:
        if kb.is_pressed('e'):
            break
        print("running")

while True:
    if kb.is_pressed('s'):
        start()
        break






