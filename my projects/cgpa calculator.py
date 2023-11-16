import sys

def main():
    cgpa_printer()

def course_creator():
    global data_list
    data_list = []
    while True:
        print('''Type a to add course | Type c to exit''')
        ans = input().strip()
        if ans == 'a':
            course_name = input('Course Name: ')
            course_point = int(input('Course Point: '))
            user_score = int(input('Your Score: '))

            data = {'course_name': course_name,
                    'course_point': course_point,
                    'user_score': user_score,
                    'user_point': user_point_calculator(user_score)}
            data_list.append(data)
        elif ans == 'c':
            return data_list

def user_point_calculator(score):
    point = 0
    if score >= 70:
        point = 4
    elif score >= 60:
        point = 3
    elif score >= 50:
        point = 2
    elif score >= 45:
        point = 1
    else:
        return point
    return point

def cgpa_calculator():
    data_list = course_creator()
    
    accumulated = 0
    overall = 0
    for data in data_list:
        accumulated += data['user_point'] * data['course_point']
        overall += data['course_point']
    cgpa = round(accumulated/overall, 2)
    return cgpa

def cgpa_printer():
    cgpa = cgpa_calculator()

    print('\n')
    print('Course name'.ljust(20) + 'Course point'.center(20) + 'Your point'.rjust(20))
    
    for data in data_list:
        print(f"{str(data['course_name']).ljust(20)}{str(data['course_point']).center(20)}{str(data['user_point']).rjust(15)}")
        
    print()
    print(f"CGPA: {cgpa}")
    
main()
                           
