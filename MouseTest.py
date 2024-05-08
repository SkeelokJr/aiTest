# first open terminal and type "pip3 install pyautogui and then pip3 install pygame"
# download GitHub Remote Repositories and GitHub push and pull extensions, 
# f1 to type "open remote repository" -> aiTest and open remote repository
# go to source control and save file to push to remote repository
# to run use "run in interactive terminal"

import pyautogui as pag
import pygame as pg

screen_size = pag.size()
screen_width, screen_height = screen_size[0], screen_size[1]
screen_centerX, screen_centerY = screen_width/2, screen_height/2

# move mouse to screen center
pag.moveTo(screen_centerX, screen_centerY)

print(screen_centerX, screen_centerY)