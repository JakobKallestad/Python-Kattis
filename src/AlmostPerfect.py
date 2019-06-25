from functools import reduce


def find_factors(n):
    return set(reduce(list.__add__,
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


while True:
    try:
        n = int(input())
        factors = find_factors(n)
        factors.remove(n)
        check = sum(factors)
        if check == n:
            print(n, "perfect")
        elif abs(check-n) <= 2:
            print(n, "almost perfect")
        else:
            print(n, "not perfect")

    except EOFError:
        break