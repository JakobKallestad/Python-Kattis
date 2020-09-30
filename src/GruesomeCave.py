from collections import deque
from copy import deepcopy

n_rows, n_cols = map(int, input().split())
map = []
map_index = []
entrance_pos = -1
diamond_pos = -1
n_empty_tiles = 0
empty_tiles = []

for i in range(n_rows):
    row = list(input())
    map_index.append(list(range(n_cols)))
    n_empty_tiles += row.count(' ')

    for j in range(len(row)):
        if row[j] == ' ':
            empty_tiles.append((i, j))

    if 'E' in row:
        entrance_pos = (i, row.index('E'))
    if 'D' in row:
        diamond_pos = (i, row.index('D'))
    map.append(row)

#print(n_empty_tiles)
print(empty_tiles)
#print(map_index)
#print(map)


def get_neighbors(pos, visited):
    neighbors = []
    if pos[0] > 0 and map[pos[0] - 1][pos[1]] != '#' and (pos[0]-1, pos[1]) not in visited:
        neighbors.append((pos[0] - 1, pos[1]))
    if pos[0] < n_rows - 1 and map[pos[0] + 1][pos[1]] != '#' and (pos[0]+1, pos[1]) not in visited:
        neighbors.append((pos[0] + 1, pos[1]))
    if pos[1] > 0 and map[pos[0]][pos[1] - 1] != '#' and (pos[0], pos[1]-1) not in visited:
        neighbors.append((pos[0], pos[1] - 1))
    if pos[1] < n_cols - 1 and map[pos[0]][pos[1] + 1] != '#' and (pos[0], pos[1]+1) not in visited:
        neighbors.append((pos[0], pos[1] + 1))
    return neighbors


def bfs(entrance_pos, diamond_pos):
    queue = deque()
    visited = {entrance_pos}
    parent = {}

    queue.append(entrance_pos)
    visited.add(entrance_pos)
    parent[entrance_pos] = None

    while queue:
        current = queue.popleft()
        for nbr in get_neighbors(current, visited):
            if nbr == diamond_pos:
                pass
            visited.add(nbr)
            parent[nbr] = current
            queue.append(nbr)

    temp = diamond_pos
    n_steps = 0
    path = []
    while temp:
        path.append(temp)
        n_steps += 1
        temp = parent[temp]
    path = path[::-1]
    assert n_steps == len(path)
    return n_steps, path


n_steps, path = bfs(entrance_pos, diamond_pos)
print(n_steps, path)

current_probs = [[1/(n_rows*n_cols) for _ in range(n_cols)] for _ in range(n_rows)]
next_probs = [[0 for _ in range(n_cols)] for _ in range(n_rows)]

#print(current_probs)

for i in range(10):
    for pos in empty_tiles:
        print(pos)
        pos_prob = current_probs[pos[0]][pos[1]]
        neighbors = get_neighbors(pos, {entrance_pos, diamond_pos})
        for nbr in neighbors:
            next_probs[nbr[0]][nbr[1]] += pos_prob/len(neighbors)
    current_probs = deepcopy(next_probs)
    #next_probs = [[0 for _ in range(n_cols)] for _ in range(n_rows)]

for i in range(n_rows):
    print(current_probs[i])




# NOT DONE YET!




