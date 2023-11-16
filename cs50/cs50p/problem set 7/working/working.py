import re
import sys

# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
# 5:00 PM to 9:00 AM
# 5 PM to 9 AM

def main():
    print(convert(input('Hours: ')))

def convert(s):
    if 'to' not in s or 'AM' not in s or 'PM' not in s:
        raise ValueError

    regex = re.compile(r'(\d+)(:\d\d)? (AM|PM) to (\d+)(:\d\d)? (AM|PM)')
    if matches := re.search(regex, s):
        if int(matches.group(1)) > 12 or int(matches.group(4)) > 12:
            raise ValueError
        if matches.group(2) and matches.group(5):
            if int(matches.group(2).strip(':')) > 59 or int(matches.group(5).strip(':')) > 59:
                raise ValueError

    start_time = convert_time_start(matches)
    end_time = convert_time_end(matches)

    return start_time + ' to ' + end_time

    
def convert_time_start(matches):
    if matches.group(3) == 'AM':
        if int(matches.group(1)) > 9:
            if matches.group(2):
                start_time = matches.group(1) + matches.group(2)
            else:
                start_time = matches.group(1) + ':00'
        else:
            if matches.group(2):
                start_time = '0' + matches.group(1) + matches.group(2)
            else:
                start_time = '0' + matches.group(1) + ':00'
    else:
        if matches.group(2):
            start_time = str(int(matches.group(1))+12) + matches.group(2)
        else:
            start_time = str(int(matches.group(1))+12) + ':00'
    return start_time

def convert_time_end(matches):
    if matches.group(6) == 'AM':
        if int(matches.group(4)) > 9:
            if matches.group(5):
                end_time = matches.group(1) + matches.group(5)
            else:
                end_time = matches.group(1) + ':00'
        else:
            if matches.group(5):
                end_time = '0' + matches.group(4) + matches.group(5)
            else:
                end_time = '0' + matches.group(4) + ':00'
    else:
        if matches.group(5):
            end_time = str(int(matches.group(4))+12) + matches.group(5)
        else:
            end_time = str(int(matches.group(4))+12) + ':00'
    return end_time

if __name__ == '__main__':
    main()
