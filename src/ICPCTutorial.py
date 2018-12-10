import math

m, n, t = map(int, input().split())

if t == 1:
    if n >= 13:
        n = math.factorial(13)
    else:
        n = math.factorial(n)
elif t == 2:
    if n >= 30:
        n = n**30
    else:
        n = 2 ** n
elif t == 3:
    n = n ** 4
elif t == 4:
    n = n ** 3
elif t == 5:
    n = n ** 2
elif t == 6:
    n = n * math.log(n, 2)
else:
    pass

print("AC") if m - n >= 0 else print("TLE")
