grid = []
for _ in range(7):
    grid.append([c for c in input()])

# visual
#for line in grid:
#    print(line)

legal_moves = 0

for y in range(7):
    for x in range(7):
        if grid[y][x] == '.':
            if x > 1 and grid[y][x-1] == 'o' and grid[y][x-2] == 'o': # from the left
                legal_moves += 1
            if x < 5 and grid[y][x+1] == 'o' and grid[y][x+2] == 'o': # from the right
                legal_moves += 1
            if y > 1 and grid[y-1][x] == 'o' and grid[y-2][x] == 'o': # from the above
                legal_moves += 1
            if y < 5 and grid[y+1][x] == 'o' and grid[y+2][x] == 'o': # from the bellow
                legal_moves += 1
print(legal_moves)