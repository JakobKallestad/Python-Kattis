from math import tan, pi

n_test_cases = int(input())
for _ in range(n_test_cases):
    n, l, d, g = map(int, input().split())
    area = ((1 / 4) * n * (l ** 2)) / tan(pi / n)
    area += pi*(d*g)**2 + n*(d*g)*l
    print(area)


