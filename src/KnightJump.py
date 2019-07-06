from collections import deque

n = int(input())
grid = [list(input()) for _ in range(n)]
visited = [[False]*n for _ in range(n)]
queue = deque()
for y in range(n):
    for x in range(n):
        if grid[y][x] == '#':
            visited[y][x] = True
        elif grid[y][x] == 'K':
            queue.append((y, x, 0))
            visited[y][x] = True

while queue:
    cy, cx, step = queue.popleft()

    # WIN
    if (cy, cx) == (0, 0):
        print(step)
        break

    # NE
    if cy-2 >= 0 and cx+1<n and not visited[cy-2][cx+1]:
        visited[cy-2][cx+1] = True
        queue.append((cy-2, cx+1, step+1))

    # EN
    if cy-1 >= 0 and cx+2<n and not visited[cy-1][cx+2]:
        visited[cy-1][cx+2] = True
        queue.append((cy-1, cx+2, step+1))

    # ES
    if cy+1 < n and cx+2<n and not visited[cy+1][cx+2]:
        visited[cy+1][cx+2] = True
        queue.append((cy+1, cx+2, step+1))

    # SE
    if cy+2<n and cx+1<n and not visited[cy+2][cx+1]:
        visited[cy+2][cx+1] = True
        queue.append((cy+2, cx+1, step+1))

    # SW
    if cy+2<n and cx-1>=0 and not visited[cy+2][cx-1]:
        visited[cy+2][cx-1] = True
        queue.append((cy+2, cx-1, step+1))

    # WS
    if cy+1<n and cx-2>=0 and not visited[cy+1][cx-2]:
        visited[cy+1][cx-2] = True
        queue.append((cy+1, cx-2, step+1))

    # WN
    if cy-1 >= 0 and cx-2>=0 and not visited[cy-1][cx-2]:
        visited[cy-1][cx-2] = True
        queue.append((cy-1, cx-2, step+1))

    # NW
    if cy-2 >= 0 and cx-1>=0 and not visited[cy-2][cx-1]:
        visited[cy-2][cx-1] = True
        queue.append((cy-2, cx-1, step+1))
else:
    print(-1)
