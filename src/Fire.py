from collections import deque

n_test_cases = int(input())
for _ in range(n_test_cases):
    w, h = map(int, input().split())
    grid = []
    burning = [[False]*w for _ in range(h)]
    visited = [[False]*w for _ in range(h)]
    you = deque()
    fire = deque()
    start_y, start_x = -1, -1
    for i in range(h):
        line = input()
        for j, c in enumerate(line):
            if c == '*':
                fire.append((i, j))
                burning[i][j] = True
            elif c == '@':
                you.appendleft((i, j))
                visited[i][j] = True
            elif c == '#':
                visited[i][j] = True
                burning[i][j] = True
        grid.append(list(line))

    escaped = False
    count = 1
    while True:
        next_you = deque()
        next_fire = deque()
        while you:
            cy, cx = you.popleft()
            if burning[cy][cx]:
                continue
            if cy == 0 or cy == h-1 or cx == 0 or cx == w-1:
                escaped = True
                break

            # north:
            if not visited[cy - 1][cx] and not burning[cy - 1][cx]:
                visited[cy - 1][cx] = True
                next_you.append((cy-1, cx))

            # east:
            if not visited[cy][cx+1] and not burning[cy][cx+1]:
                visited[cy][cx+1] = True
                next_you.append((cy, cx+1))

            # south:
            if not visited[cy + 1][cx] and not burning[cy + 1][cx]:
                visited[cy + 1][cx] = True
                next_you.append((cy+1, cx))

            # west:
            if not visited[cy][cx-1] and not burning[cy][cx-1]:
                visited[cy][cx-1] = True
                next_you.append((cy, cx-1))

        # escaped
        if escaped:
            print(count)
            break

        # lost to fire
        if not next_you:
            print("IMPOSSIBLE")
            break
        you = next_you

        while fire:
            cy, cx = fire.popleft()
            # north:
            if cy > 0 and not burning[cy - 1][cx]:
                burning[cy-1][cx] = True
                next_fire.append((cy-1, cx))

            # east:
            if cx < w - 1 and not burning[cy][cx + 1]:
                burning[cy][cx+1] = True
                next_fire.append((cy, cx+1))

            # south:
            if cy < h - 1 and not burning[cy + 1][cx]:
                burning[cy+1][cx] = True
                next_fire.append((cy+1, cx))

            # west:
            if cx > 0 and not burning[cy][cx - 1]:
                burning[cy][cx-1] = True
                next_fire.append((cy, cx-1))
        fire = next_fire

        count += 1



