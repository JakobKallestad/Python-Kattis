from functools import reduce


def find_factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


n = int(input())
factors = find_factors(n)
factors = sorted(factors)
for f in factors:
    print(f-1, end=' ')
print()