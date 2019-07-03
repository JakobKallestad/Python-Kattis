h, w = map(int, input().split())
grid = [list(input()) for _ in range(h)]
visited = [[False]*w for _ in range(h)]
flooded = [[False]*w for _ in range(h)]
end_y, end_x = -1, -1
flood = []
you = []
for y in range(h):
    for x in range(w):
        if grid[y][x] == '*':
            flooded[y][x] = True
            flood.append((y, x))
        elif grid[y][x] == 'S':
            visited[y][x] = True
            you.append((y, x))
        elif grid[y][x] == 'D':
            end_y, end_x = y, x
            flooded[y][x] = True
        elif grid[y][x] == 'X':
            visited[y][x] = True
            flooded[y][x] = True

escaped = False
count = 0
while True:
    next_flood = []
    next_you = []

    # check at startup if flooded or if y, x == end_y, end_x
    while you:
        cy, cx = you.pop()
        # escaped:
        if cy == end_y and cx == end_x:
            escaped = True
            break
        # flooded:
        if flooded[cy][cx]:
            continue
        # North
        if cy > 0 and not visited[cy-1][cx]:# and not flooded[cy-1][cx]:
            visited[cy-1][cx] = True
            next_you.append((cy-1, cx))

        # East
        if cx < w-1 and not visited[cy][cx+1]:# and not flooded[cy][cx+1]:
            visited[cy][cx+1] = True
            next_you.append((cy, cx+1))

        # South
        if cy < h-1 and not visited[cy+1][cx]:# and not flooded[cy+1][cx]:
            visited[cy + 1][cx] = True
            next_you.append((cy + 1, cx))

        # West
        if cx > 0 and not visited[cy][cx-1]:# and not flooded[cy][cx-1]:
            visited[cy][cx-1] = True
            next_you.append((cy, cx-1))

    # Check if escaped
    if escaped:
        print(count)
        break

    # Check if all hope is lost:
    if not next_you:
        print("KAKTUS")
        break

    while flood:
        cy, cx = flood.pop()
        # North
        if cy > 0 and not flooded[cy - 1][cx]:
            flooded[cy - 1][cx] = True
            next_flood.append((cy - 1, cx))

        # East
        if cx < w - 1 and not flooded[cy][cx + 1]:
            flooded[cy][cx + 1] = True
            next_flood.append((cy, cx + 1))

        # South
        if cy < h - 1 and not flooded[cy + 1][cx]:
            flooded[cy + 1][cx] = True
            next_flood.append((cy + 1, cx))

        # West
        if cx > 0 and not flooded[cy][cx - 1]:
            flooded[cy][cx - 1] = True
            next_flood.append((cy, cx - 1))

    # prepare for next iteration
    count += 1
    you = next_you
    flood = next_flood
