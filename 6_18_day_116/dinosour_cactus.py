import time
import pyautogui
from PIL import ImageGrab


GAME_REGION = (100, 300, 600, 400)

CACTUS_COLOR = (83, 83, 83)

def is_cactus_present():
    screen = ImageGrab.grab(bbox=GAME_REGION)
    screen_rgb = screen.convert('RGB')

    for x in range(screen_rgb.width):
        for y in range(screen_rgb.height):
            if screen_rgb.getpixel((x, y)) == CACTUS_COLOR:
                return True
    return False

def main():
    print("Starting the T-Rex game automation...")
    time.sleep(2)

    while True:
        if is_cactus_present():
            print("Cactus detected! Jumping...")
            pyautogui.press('space')
            time.sleep(0.1)

main()
