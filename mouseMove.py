import pyautogui
from win32api import GetSystemMetrics

def mouseMove():
    x = GetSystemMetrics(0)
    y = GetSystemMetrics(1)
    pyautogui.moveTo(x-(x*1/15), y-(y*8/10), duration=2)
    pyautogui.scroll(-1000) #-1000 is good 

if __name__ == "__main__":
    mouseMove()