import sys
import time

import pyautogui
from numpy import array
from PIL import ImageGrab, ImageOps


class Coordinates():
    replay_button = (480,580)
    dino = (220, 585)
    low = (230, 600)

def restart_game():
    pyautogui.click(Coordinates.replay_button)

def jump(counter):
    sys.stdout.write("\nJump " + str(counter))
    pyautogui.keyDown('space')
    time.sleep(0.05)
    pyautogui.keyUp('space')

def image_grab():
    box = (Coordinates.dino[0] + 140, Coordinates.dino[1],
           Coordinates.dino[0] + 180, Coordinates.dino[1] + 30)
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    return a.sum()

def main():
    restart_game()
    count = 0
    while True:
        if(image_grab() != 1447):
            count +=1
            jump(count)
            time.sleep(0.05)

if __name__ == "__main__":
    main()
