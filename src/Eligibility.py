n = int(input())
for i in range(n):
    name, course_start, date_of_birth, n_courses = input().split()
    if int(course_start[:4]) >= 2010:
        print(name,'eligible')
    elif int(date_of_birth[:4]) >= 1991:
        print(name,'eligible')
    elif int(n_courses) >= 41:
        print(name,'ineligible')
    else:
        print(name,'coach petitions')
