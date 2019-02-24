import sys
import time

import pyautogui
from numpy import array
from PIL import ImageGrab, ImageOps


class Coordinates():
    # Pixel location on screen of restart button
    replay_button = (480, 580)
    # Pixel location just infront of dino
    dino = (220, 585)


def restart_game():
    # Click to restart and begin game
    pyautogui.click(Coordinates.replay_button)


def jump(counter):
    # Return number of jumps to console
    print("Jump #" + str(counter))
    sys.stdout.flush()
    # Initiate jump
    pyautogui.keyDown('space')
    time.sleep(0.05)
    # End jump
    pyautogui.keyUp('space')


def image_grab():
    # Analyze 40x30 grid in front of dinosaur and return sum of pixel values
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
        # If total pixel values are > 1447, jump
        if(image_grab() != 1447):
            count += 1
            jump(count)
            time.sleep(0.05)


if __name__ == "__main__":
    main()
