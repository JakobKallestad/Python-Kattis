n = int(input())
for i in range(n):
    case, num = map(int, input().split())
    print(case, int(num*(num+1)/2), int(num**2), int(num*(num+1)))
