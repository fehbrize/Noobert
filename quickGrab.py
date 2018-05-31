from PIL import ImageGrab
import time
import os


def screen_grab():
    box = ()
    im = ImageGrab.grab()
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')


def main():
    screen_grab()


if __name__ == '__main__':
    main()