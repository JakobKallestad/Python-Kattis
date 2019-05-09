from math import log, e, sqrt, pi

limit = 10**5
current = 0
d2 = 0
factorials = [None]
for i in range(1, limit+1):
    current += log(i)
    factorials.append(current)

while True:
    n = int(input())
    if n == 0:
        break
    approx = log(sqrt(2*pi*n)) + (log(n)-1)*n
    final = factorials[n] - approx
    print(e**final)
