n = int(input())
ab_list = ['A']

for i in range(n):
    new_list = []
    a_count = 0
    b_count = 0
    for e in ab_list:
        if e == 'A':
            new_list.append('B')
            b_count += 1
        else:
            new_list.append('B')
            new_list.append('A')
            a_count += 1
            b_count += 1
    ab_list = new_list[:]
print(a_count,b_count)