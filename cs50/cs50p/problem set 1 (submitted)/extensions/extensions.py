import re

def main():
    file_name = input('File name: ').strip().lower()
    print(type_finder(file_name))

def type_finder(filename):
    if '.' not in filename:
        return 'application/octet-stream'
    
    regex_obj = re.compile(r'(\w|\.)+(\.[a-zA-Z]+)')
    if match := re.search(regex_obj, filename):
        file_type = match.group(2)

    if file_type == '.gif':
        return 'image/gif'
    elif file_type == '.jpg' or file_type == '.jpeg':
        return 'image/jpeg'
    elif file_type == '.png':
        return 'image/png'
    elif file_type == '.pdf':
        return 'application/pdf'
    elif file_type == '.txt':
        return 'application/txt'
    elif file_type == '.zip':
        return 'application/zip'

main()
