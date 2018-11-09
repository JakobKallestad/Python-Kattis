n = int(input())
qaly = 0
for i in range(n):
    xy = list(map(float, input().split()))
    qaly += xy[0]*xy[1]
print(qaly)