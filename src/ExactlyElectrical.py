a, b = map(int, input().split())
c, d = map(int, input().split())
charges = int(input())

diff_x = abs(a-c)
diff_y = abs(b-d)
total_diff = diff_x+diff_y

if charges < total_diff:
    print('N')
elif (total_diff-charges) % 2 == 0:
    print('Y')
else:
    print('N')