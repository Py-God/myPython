from datetime import datetime
from num2words import num2words

def main():
    birthday = input('Date of Birth: ').strip()
    print(num2words(calculator(birthday)), 'minutes')
 
def calculator(s):
    if '-' in s:
        year, month, day = map(int, s.split('-'))
        birthday = datetime(year, month, day)
        time_difference =  datetime.now() - birthday
        
        total_minutes = int(time_difference.total_seconds() / 60)
        return round(total_minutes)
    

if __name__ == '__main__':
    main()
