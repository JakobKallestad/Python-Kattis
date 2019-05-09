import math

n = int(input())
m = math.ceil(n/2)
print((m+1)**2) if n % 2 == 0 else print(m*(m+1))
