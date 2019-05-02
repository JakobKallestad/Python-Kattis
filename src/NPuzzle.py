grid = []
for _ in range(4):
    grid.append(list(input()))

correct_grid = {'A': (0, 0), 'B': (0, 1), 'C': (0, 2), 'D': (0, 3),
                'E': (1, 0), 'F': (1, 1), 'G': (1, 2), 'H': (1, 3),
                'I': (2, 0), 'J': (2, 1), 'K': (2, 2), 'L': (2, 3),
                'M': (3, 0), 'N': (3, 1), 'O': (3, 2)}

total_off = 0
for y in range(4):
    for x in range(4):
        c = grid[y][x]
        if c == '.':
            continue
        d = correct_grid[c]
        total_off += (abs(y - d[0]) + abs(x - d[1]))
print(total_off)
