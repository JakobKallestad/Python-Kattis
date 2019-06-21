'''
3 2
0123 9876 2222
2 1 8888 2222
3 2 9876 2222 7654
3 2
0123 9876 2222
2 2 8888 2222
3 2 7654 9876 2222
0
'''

while True:
    try:
        n_courses, n_categories = map(int, input().split())
    except:
        break
    courses = set(map(int, input().split()))
    all_good = True
    for _ in range(n_categories):
        cat = list(map(int, input().split()))
        n_required = cat[1]
        cat = set(cat[2:])
        if len(courses.intersection(cat)) < n_required:
            all_good = False
    print("yes") if all_good else print("no")
