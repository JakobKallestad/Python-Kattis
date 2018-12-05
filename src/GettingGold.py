from queue import Queue

cols, rows = map(int, input().split())
grid = []
start_pos = []
for i in range(rows):
    row = []
    for j, c in enumerate(input()):
        if c == 'P':
            start_pos = [i, j]
        row.append(c)
    grid.append(row)
#[print(line) for line in grid] # visual test

gold = 0
visited = [[False for _ in range(cols)] for _ in range(rows)]
#[print(line) for line in visited] # visual test
queue = Queue()
queue.put(start_pos)
while not queue.empty():
    current = queue.get()
    y, x = current[0], current[1]

    # need to check all directions:
    moveable = ((y == 0 or grid[y - 1][x] != 'T') and (y == rows - 1 or grid[y + 1][x] != 'T')
                and (x == cols - 1 or grid[y][x + 1] != 'T') and (x == 0 or grid[y][x - 1] != 'T'))


    if moveable:
        # up
        if y != 0 and (grid[y-1][x] == '.' or grid[y-1][x] == 'G') and not visited[y-1][x]:
            if grid[y-1][x] == 'G':
                gold += 1
            queue.put([y-1, x])
            visited[y-1][x] = True

        # down
        if y != rows-1 and (grid[y+1][x] == '.' or grid[y+1][x] == 'G') and not visited[y+1][x]:
            if grid[y+1][x] == 'G':
                gold += 1
            queue.put([y+1, x])
            visited[y+1][x] = True

        # right
        if x != cols-1 and (grid[y][x+1] == '.' or grid[y][x+1] == 'G') and not visited[y][x+1]:
            if grid[y][x+1] == 'G':
                gold += 1
            queue.put([y, x+1])
            visited[y][x+1] = True

        # left
        if x != 0 and (grid[y][x-1] == '.' or grid[y][x-1] == 'G') and not visited[y][x-1]:
            if grid[y][x-1] == 'G':
                gold += 1
            queue.put([y, x-1])
            visited[y][x-1] = True

print(gold)

