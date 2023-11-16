Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import send2trash
baconFile = open('bacon.txt', 'a')  # creates the file
baconFile.write('Bacon is not a vegetable.')
25
baconFile.close()
send2trash.send2trash('bacon.txt')
