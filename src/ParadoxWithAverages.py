n_test_cases = int(input())
for _ in range(n_test_cases):
    input()
    input()
    cs_students = list(map(int, input().split()))
    economy_students = list(map(int, input().split()))
    cs_total = sum(cs_students)
    economy_total = sum(economy_students)
    cs_mean = cs_total / len(cs_students)
    economy_mean = economy_total / len(economy_students)
    count = 0
    for student in cs_students:
        left_mean = (cs_total-student) / (len(cs_students)-1)
        joined_mean = (economy_total+student) / (len(economy_students)+1)
        if left_mean > cs_mean and joined_mean > economy_mean:
            count += 1
    print(count)
