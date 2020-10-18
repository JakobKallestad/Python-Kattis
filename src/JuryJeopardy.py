directions = [
    (-1, 0),
    (0, 1),
    (1, 0),
    (0, -1)
]

n_test_cases = int(input())
print(n_test_cases)
for _ in range(n_test_cases):
    visited = []
    seq = list(input())
    c_pos = [0, 0]
    c_dir = 1
    for s in seq:
        visited.append(c_pos)
        if s == 'R':
            c_dir = (c_dir+1) % 4
        elif s == 'L':
            c_dir = (c_dir-1) % 4
        elif s == 'B':
            c_dir = (c_dir+2) % 4
        c_pos = [cord + diff for cord, diff in zip(c_pos, directions[c_dir])]

    x_max = max(visited, key=lambda pos: pos[1])[1]
    x_min = min(visited, key=lambda pos: pos[1])[1]
    y_max = max(visited, key=lambda pos: pos[0])[0]
    y_min = min(visited, key=lambda pos: pos[0])[0]
    height = y_max-y_min+3
    width = x_max-x_min+2

    grid = [['#']*width for _ in range(height)]
    for y, x in visited:
        grid[y+1-y_min][x] = '.'

    print(height, width)
    for row in grid:
        print(''.join(row))
