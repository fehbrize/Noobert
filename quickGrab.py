from PIL import ImageGrab
import time
import os


def screen_grab():
    box = ()
    im = ImageGrab.grab()
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')


def main():
    print("hi, im noobert owo")
    screen_grab()
    print("scweenshot compwete! uwu")


if __name__ == '__main__':
    main()