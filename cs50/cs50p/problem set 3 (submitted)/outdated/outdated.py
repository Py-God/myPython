months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
        ]
def main():
    date = input('Date: ').strip()
    print(sorter(date))

def sorter(date):
    if '/' in date:
        month, day, year = date.split('/')
        print(month)
        if month in months or int(month) > 12 or int(month) < 1 or int(day) > 31 or int(day) < 1:
            main()

        if len(month) < 2 and len(day) < 2:
            return f'{year}-0{month}-0{day}'
        if len(month) < 2 and len(day) == 2:
            return f'{year}-0{month}-{day}'
        if len(month) == 2 and len(day) < 2:
            return f'{year}-{month}-0{day}'
        return f'{year}-{month}-{day}'

    if ',' not in date:
        main()
    month, day, year = date.split()
    if month not in months or len(year) < 4 or int(day.strip(',')) > 31:
        main()

    month_index = months.index(month)
    if month_index+1 < 10 and len(day) < 3:
        return f'{year}-0{month_index+1}-0{day.strip(",")}'
    if month_index+1 < 10 and len(day) == 3:
        return f'{year}-0{month_index+1}-{day.strip(",")}'
    if month_index+1 >= 10 and len(day) < 3:
        return f'{year}-{month_index+1}-0{day.strip(",")}'
    return f'{year}-{month_index+1}-{day.strip(",")}'

main()


