import math

while True:
    a, b, c = map(float, input().split())
    if a == b == c == 0:
        break
    print(a**2*math.pi, end=' ')
    print((2*a)**2*(c/b))