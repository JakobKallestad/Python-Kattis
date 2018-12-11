from collections import deque

r, c, n = map(int, input().split())
grid = [[False for _ in range(c)] for _ in range(r)]
day_count = 1
invades_today = 0
invades_tomorrow = 0
q = deque()

for _ in range(n):
    y, x = map(int, input().split())  # spies already in square country
    y, x = y-1, x-1
    grid[y][x] = True  # True for occupied
    q.append((y, x))
    invades_today += 1

while True:
    if all(all(i for i in row) for row in grid):  # if all conquered
        break
    while invades_today > 0:
        invades_today -= 1
        y, x = q.pop()
        if y > 0 and not grid[y - 1][x]:
            grid[y - 1][x] = True
            q.appendleft((y-1, x))
            invades_tomorrow += 1
        if y < r-1 and not grid[y + 1][x]:
            grid[y + 1][x] = True
            q.appendleft((y+1, x))
            invades_tomorrow += 1
        if x > 0 and not grid[y][x-1]:
            grid[y][x-1] = True
            q.appendleft((y, x-1))
            invades_tomorrow += 1
        if x < c-1 and not grid[y][x+1]:
            grid[y][x+1] = True
            q.appendleft((y, x+1))
            invades_tomorrow += 1
    day_count += 1
    invades_today = invades_tomorrow
    invades_tomorrow = 0

print(day_count)
