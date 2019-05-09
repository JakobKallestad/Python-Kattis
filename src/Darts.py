import math
from bisect import bisect

n_test_cases = int(input())
thresholds = [20*(11-i) for i in range(10, 0, -1)]
for _ in range(n_test_cases):
    score = 0
    n_darts = int(input())
    for _ in range(n_darts):
        x, y = map(int, input().split())
        dist = math.sqrt(x**2 + y**2)
        score += 10-bisect(thresholds, dist-0.000001)  # annoying, but I have to subtract delta
    print(score)