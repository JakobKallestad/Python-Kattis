n = int(input())
for i in range(n):
    case, days = map(int, input().split())
    print(case, int(days+(days*(days+1))/2))