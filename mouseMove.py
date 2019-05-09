import pyautogui
from win32api import GetSystemMetrics

def moveNscroll(val, x=None, y=None, duration=1):
    if x==None or y==None:
    # if no x and y value given it will automaticly detect your screen size and move mouse to near to the top right of the screen and scroll
        x = GetSystemMetrics(0)
        y = GetSystemMetrics(1)
        pyautogui.moveTo(x-(x*1/15), y-(y*8/10), duration)
    else: 
        pyautogui.moveTo(x, y, duration)
    pyautogui.scroll(val)

# if __name__ == "__main__":
#     moveNscroll(100)