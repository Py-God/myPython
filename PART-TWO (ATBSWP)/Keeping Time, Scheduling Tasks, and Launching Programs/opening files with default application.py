Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
fileObj = open('hello.txt', 'w')
fileObj.Write('Hello world!')
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    fileObj.Write('Hello world!')
AttributeError: '_io.TextIOWrapper' object has no attribute 'Write'. Did you mean: 'write'?
fileObj.write('Hello world!')
12
fileObj.close()
import subprocess
subprocess.Popen(['start', 'hello.txt'], shell=True)
<Popen: returncode: None args: ['start', 'hello.txt']>
