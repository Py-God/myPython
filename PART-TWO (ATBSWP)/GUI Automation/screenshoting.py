Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import pyautogui
im = pyautogui.screenshot()
im.getpixel((0, 0))
(46, 46, 46)
im.getpixel((50, 200))
(51, 51, 51)
