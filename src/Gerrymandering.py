p, d = map(int, input().split())
districts = [[0, 0] for i in range(d)]
for _ in range(p):
    di, a, b = map(int, input().split())
    districts[di-1][0] += a
    districts[di-1][1] += b

v, wa, wb = 0, 0, 0
for i in range(d):
    a, b = districts[i]
    v += (a+b)
    midpoint = ((a+b)//2 + 1)
    if a < midpoint:
        print("B", a, b-midpoint)
        wa += a
        wb += b-midpoint
    else:
        print("A", a-midpoint, b)
        wa += a-midpoint
        wb += b
print(abs(wa-wb)/v)
