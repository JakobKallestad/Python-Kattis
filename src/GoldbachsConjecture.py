def SieveOfEratosthenes(n):
    prime = [True for _ in range(n + 1)]
    primes = set()
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * 2, n + 1, p):
                prime[i] = False
        p += 1
    for p in range(2, n):
        if prime[p]:
            primes.add(p)
    return primes


primes = SieveOfEratosthenes(32000)
n_test_cases = int(input())
for _ in range(n_test_cases):
    n = int(input())
    representations = set()
    for p in primes:
        if n - p in primes:
            representations.add((min(p, n-p), max(p, n-p)))
    representations = sorted(representations)
    print(n, "has", len(representations), "representation(s)")
    for (a, b) in representations:
        print(a, '+', b, sep='')
    print()
