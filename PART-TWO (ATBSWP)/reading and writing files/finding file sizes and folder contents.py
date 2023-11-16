Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import os
os.path.getsize('C:\\Games\\Pro_Evolution_Soccer_2017\\setup.exe')
722610
os.listdir('C:\\Games\\Pro_Evolution_Soccer_2017')
['autorun.inf', 'CheckSums_so.txt', 'Crack', 'Game_Setup_DVD.iso', 'icon.ico', 'Password.txt', 'Read me - How To Install.txt', 'setup-1a.bin', 'setup-1b.bin', 'setup-1c.bin', 'setup-1d.bin', 'setup-1e.bin', 'setup-2a.bin', 'setup-2b.bin', 'setup.exe', 'Step 1 - Disable Defender.exe', 'Step 1 - Disable Defender.ini', 'Step 2 - Extract Setup.rar', 'wrar591.exe']

totalSize = 0
for filename in os.listdir('C:\\Games\\Pro_Evolution_Soccer_2017'):
    totalSize = totalSize + os.path.getsize(os.path.join('C:\\Games\\Pro_Evolution_Soccer_2017', filename))

print(totalSize)
23180545541
