while True:
    r, c = map(int, input().split())
    if r == c == 0:
        break
    cols = [""]*c
    for i in range(r):
        line = input()
        for j in range(c):
            cols[j] += line[j]
    cols = sorted(cols, key=lambda s: s.lower())
    for i in range(r):
        for j in range(c):
            print(cols[j][i], end='')
        print()

