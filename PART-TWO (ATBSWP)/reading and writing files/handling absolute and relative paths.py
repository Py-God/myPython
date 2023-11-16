Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import os
os.path.abspath('.')
'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python310'
os.path.abspath('.\\Scripts')
'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python310\\Scripts'
os.path.isabs('.')
False
os.path.isabs(os.path.abspath('.'))
True

os.path.relpath('C:\\Games', 'C:\\')
'Games'
os.path.relpath('C:\\Games', 'C:\\spam\\eggs')
'..\\..\\Games'
os.getcwd()
'C:\\Users\\user\\AppData\\Local\\Programs\\Python\\Python310'


path = 'C:\\Games\\Sim.City\\Password.txt'
os.path.basename(path)
'Password.txt'
os.path.dirname(path)
'C:\\Games\\Sim.City'
passFileName = 'C:\\Games\\Sim.City\\Password.txt'
os.path.split(passFileName)
('C:\\Games\\Sim.City', 'Password.txt')
(os.path.dirname(passFileName), os.path.basename(passFileName))
('C:\\Games\\Sim.City', 'Password.txt')
passFileName.split(os.path.sep)
['C:', 'Games', 'Sim.City', 'Password.txt']
