from PIL import ImageGrab
import time
import os
import win32api, win32con

# Globals
# --------------------------

x_pad = 464
y_pad = 243


def screen_grab():
    box = (x_pad + 1, y_pad + 1, x_pad + 640, y_pad + 480)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')


def left_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    print('Click owo')


def left_down():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(.1)
    print('left down ^u^')


def left_up():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    time.sleep(.1)
    print('left release ^w^')


def mouse_pos(cord):
    win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))


def get_cords():
    x, y = win32api.GetCursorPos()
    x = x - x_pad
    y = y-y_pad
    print(x, y)


def start_game():
    #first menu
    mouse_pos((338, 203))
    left_click()
    time.sleep(.1)

    #second menu
    mouse_pos((306, 380))
    left_click()
    time.sleep(.1)

    #third menu
    mouse_pos((599, 457))
    left_click()
    time.sleep(.1)

    #fourth menu
    mouse_pos((301, 379))
    left_click()
    time.sleep(.1)


def main():
    pass


if __name__ == '__main__':
    main()
