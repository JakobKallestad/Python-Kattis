while True:
    h, t = map(int, input().split())
    n_moves = 0
    if h == t == 0:
        break

    while not (h == t == 0):
        n_moves += 1
        if h >= 2:
            h -= 2
        elif t >= 2:
            t -= 2
            h += 1
        elif t <= 2:
            t += 1
    print(n_moves)
