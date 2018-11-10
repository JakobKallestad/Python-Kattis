import math

import sys

n = int(input())
if n >1000:
    print(math.e)
    sys.exit()
euler = 0
for i in range(n+1):
    euler += (1/math.factorial(i))
print(euler)
