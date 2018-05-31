from PIL import ImageGrab
import time
import os

# Globals
# --------------------------

x_pad = 464
y_pad = 243


def screen_grab():
    box = (x_pad + 1, y_pad + 1, x_pad + 640, y_pad + 480)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')


def main():
    print("hi, im noobert owo")
    screen_grab()
    print("scweenshot compwete! uwu")


if __name__ == '__main__':
    main()