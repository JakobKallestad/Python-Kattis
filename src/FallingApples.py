r, c = map(int, input().split())
grid = [list(input()) for _ in range(r)]
trans_grid = list(map(list, zip(*grid[::-1])))

for y in range(c):
    first_open = 0
    for x in range(r):
        if trans_grid[y][x] == 'a':
            trans_grid[y][x] = '.'
            trans_grid[y][first_open] = 'a'
            first_open += 1
        elif trans_grid[y][x] == '#':
            first_open = x+1

grid = list(map(list, zip(*trans_grid)))[::-1]
for row in grid:
    print(''.join(row))
