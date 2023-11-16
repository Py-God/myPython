Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import os
os.path.exists('C:\\Windows')
True
os.path.exists('C:\\Windows\\yomama')
False
os.path.isdir('C:\\Windows\\System32')
True
os.path.isfile('C:\\Windows\\System32')
False
os.path.isdir('C:\\Games\\Pro_Evolution_Soccer_2017\\setup.exe')
False
os.path.isfile('C:\\Games\\Pro_Evolution_Soccer_2017\\setup.exe')
True

os.path.exists('D:\\')
False
# to check for a hardrive connectsed to the computer