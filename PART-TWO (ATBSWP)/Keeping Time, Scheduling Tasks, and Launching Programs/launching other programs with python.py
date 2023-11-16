Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import subprocess
subprocess.Popen('C:\\Windows\\System32\\calc.exe')
<Popen: returncode: None args: 'C:\\Windows\\System32\\calc.exe'>
calcProc = subprocess.Popen('C:\\Windows\\System32\\calc.exe')
calcProc.poll() == None
False
calcProc.wait()
0
calcProc.poll()
0
calcProc.wait()
0
calcProc.poll()
0
