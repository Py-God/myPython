Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import json
 stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
 
SyntaxError: unexpected indent
stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felineIQ": null}'
jsonDataAsPythonValue = json.loads(stringOfJsonData)
jsonDataAsPythonValue
{'name': 'Zophie', 'isCat': True, 'miceCaught': 0, 'felineIQ': None}
