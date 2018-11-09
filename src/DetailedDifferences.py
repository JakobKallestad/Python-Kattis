n = int(input())
for i in range(n):
    fin_list = []
    line1 = input()
    line2 = input()
    for a,b in zip(line1, line2):
        if a == b:
            fin_list.append('.')
        else:
            fin_list.append('*')
    print(line1)
    print(line2)
    print(''.join(fin_list))
    print()