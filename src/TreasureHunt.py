from collections import deque

n_rows, n_cols = map(int, input().split())
grid = []
visited = [[False] * n_cols for _ in range(n_rows)]
for _ in range(n_rows):
    grid.append(list(input()))

p_x, p_y = 0, 0


def bfs(p_y, p_x, moves):
    queue = deque()
    queue.append((p_y, p_x))
    visited[p_y][p_x] = True
    n_moves = 0
    while queue:
        c_y, c_x = queue.pop()
        v = moves[grid[c_y][c_x]](c_y, c_x, queue, visited, n_moves)
        if v is not None:
            return v
        n_moves += 1


def move_north(c_y, c_x, queue, visited, n_moves):
    if c_y - 1 < 0:
        return "Out"
    elif visited[c_y - 1][c_x]:
        return "Lost"
    else:
        visited[c_y - 1][c_x] = True
        queue.append((c_y - 1, c_x))


def move_south(c_y, c_x, queue, visited, n_moves):
    if c_y + 1 >= n_rows:
        return "Out"
    elif visited[c_y + 1][c_x]:
        return "Lost"
    else:
        visited[c_y + 1][c_x] = True
        queue.append((c_y + 1, c_x))


def move_west(c_y, c_x, queue, visited, n_moves):
    if c_x - 1 < 0:
        return "Out"
    elif visited[c_y][c_x - 1]:
        return "Lost"
    else:
        visited[c_y][c_x - 1] = True
        queue.append((c_y, c_x - 1))


def move_east(c_y, c_x, queue, visited, n_moves):
    if c_x + 1 >= n_cols:
        return "Out"
    elif visited[c_y][c_x + 1]:
        return "Lost"
    else:
        visited[c_y][c_x + 1] = True
        queue.append((c_y, c_x + 1))


def find_treassure(c_y, c_x, queue, visisted, n_moves):
    return n_moves


moves = {'N': move_north, 'S': move_south, 'W': move_west, 'E': move_east, 'T': find_treassure}
print(bfs(p_x, p_y, moves))
