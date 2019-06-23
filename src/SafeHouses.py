from collections import deque

length = int(input())
grid = []
for _ in range(length):
    grid.append(list(input()))
#print(grid)


spies = []
houses = []
for y in range(length):
    for x in range(length):
        if grid[y][x] == 'H':
            houses.append((y, x))
        if grid[y][x] == 'S':
            spies.append((y, x))


def bfs(houses):
    dist_to_houses = [[float('inf')]*length for _ in range(length)]
    queue = deque()
    for h in houses:
        dist_to_houses[h[0]][h[1]] = 0
        queue.append((*h, 0))

    while queue:
        currentY, currentX, dist = queue.popleft()
        # UP
        if currentY > 0 and dist_to_houses[currentY-1][currentX] == float('inf'):
            dist_to_houses[currentY-1][currentX] = dist+1
            queue.append((currentY-1, currentX, dist+1))
        # RIGHT
        if currentX < length-1 and dist_to_houses[currentY][currentX+1] == float('inf'):
            dist_to_houses[currentY][currentX+1] = dist+1
            queue.append((currentY, currentX+1, dist+1))
        # DOWN
        if currentY < length-1 and dist_to_houses[currentY+1][currentX] == float('inf'):
            dist_to_houses[currentY+1][currentX] = dist+1
            queue.append((currentY+1, currentX, dist+1))
        # LEFT
        if currentX > 0 and dist_to_houses[currentY][currentX-1] == float('inf'):
            dist_to_houses[currentY][currentX-1] = dist+1
            queue.append((currentY, currentX-1, dist+1))
    return dist_to_houses


dist_to_houses = bfs(houses)
m_dist = 0
for s in spies:
    m_dist = max(m_dist, dist_to_houses[s[0]][s[1]])
print(m_dist)

