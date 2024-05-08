# first open terminal and type "pip install pyautogui" and "pip install keyboard"
# also do pip install opencv-pythons

import pyautogui as pag
import keyboard as kb
import webbrowser as web
import time

running = True

screen_size = pag.size()
screen_width, screen_height = screen_size[0], screen_size[1]
screen_centerX, screen_centerY = screen_width/2, screen_height/2
game_width, game_height = 540, 480
game_x, game_y = 0, 0

url = "https://www.google.com/search?q=minesweeper&sca_esv=a0ffaebd0ed0b666&sca_upv=1&source=hp&ei=fPA6ZryeJpTRkPIP_cKliA4&iflsig=AL9hbdgAAAAAZjr-jPeFYpelOKIwox0HrNxp3BrCINvA&ved=0ahUKEwi8zKbAjf2FAxWUKEQIHX1hCeEQ4dUDCA8&uact=5&oq=minesweeper&gs_lp=Egdnd3Mtd2l6IgttaW5lc3dlZXBlcjILEC4YgAQYsQMYgwEyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyCBAAGIAEGLEDMggQABiABBixAzIIEAAYgAQYsQMyCxAAGIAEGLEDGIMBMgUQABiABDIFEAAYgARIpw1QAFiqDHAAeACQAQCYAVGgAfAEqgECMTG4AQPIAQD4AQGYAgugAo0FwgIOEAAYgAQYsQMYgwEYigXCAg4QLhiABBixAxjRAxjHAcICCxAuGIAEGNEDGMcBwgIREC4YgAQYsQMY0QMYgwEYxwHCAhAQLhiABBixAxiDARiKBRgKwgIIEC4YgAQYsQPCAgcQLhiABBgKmAMAkgcCMTGgB8Fv&sclient=gws-wiz&safe=active"

def start():
    global game_x, game_y
    print("START")
    web.open(url, new=0, autoraise=True)
    time.sleep(1)
    testX, testY = pag.locateCenterOnScreen('play_button.png', confidence=0.8)
    pag.moveTo(testX, testY)
    pag.click()
    time.sleep(0.1)
    game = pag.locateOnScreen("minesweeper_ui.png", confidence=0.97)
    game_x, game_y = game[0], game[1]
    pag.moveTo(game_x, game_y)
    while True:
        if kb.is_pressed('e'):
            pag.hotkey('ctrl', 'shift', 'w')
            print("STOP")
            break

while True:
    if kb.is_pressed('s'):
        start()
        break






