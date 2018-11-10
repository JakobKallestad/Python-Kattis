while True:
    n, x = map(int, input().split())
    if n == 0 and x == 0:
        break
    print(int(n/x),n%x,'/',x)
