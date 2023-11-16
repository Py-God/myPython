Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import shutil
shutil.move('C:\\bacon\\bacon.txt', 'C:\\eggs')
'C:\\eggs\\bacon.txt'

shutil.move('C:\\bacon\\bacon.txt', 'C:\\eggs\\new_bacon.txt')
'C:\\eggs\\new_bacon.txt'
# This line says, “Move C:\bacon.txt into the folder C:\eggs, and while you’re at it, rename that bacon.txt file to new_bacon.txt.”

shutil.move('C:\\bacon\\bacon1.txt', 'C:\\egg')
# you cant create a file in the root directory of your harddrive

shutil.move('C:\\bacon\\bacon1.txt', 'C:\\eggs\\new_bacon')
'C:\\eggs\\new_bacon'
