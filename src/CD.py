while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    jack = {int(input()) for _ in range(n)}
    total = sum(1 for _ in range(m) if int(input()) in jack)
    print(total)

# This only works in python2. Replace input() with raw_input() in order to translate it to python2
