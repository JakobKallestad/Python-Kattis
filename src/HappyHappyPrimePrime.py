def sieveOfEratosthenes(n):
    prime = [True for _ in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[1] = False
    return prime


prime = sieveOfEratosthenes(10000)


def check_happy(i):
    visited = set()
    while True:
        si = list(map(int, list(str(i))))
        total = 0
        for n in si:
            total += n**2
        if total == 1:
            return True
        if total in visited:
            return False
        visited.add(total)
        i = total


n_test_cases = int(input())
for _ in range(n_test_cases):
    nr, num = map(int, input().split())
    print(nr, num, "YES" if prime[num] and check_happy(num) else "NO")

