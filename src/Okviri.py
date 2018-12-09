line = input()
width = len(line)*4+1
grid = [[] for _ in range(5)]
for i in range(5):
    grid[i] = ['.']*width
    if i == 0 or i == 4:
        grid[i][2::4] = ['#']*len(line)
    elif i == 1 or i == 3:
        grid[i][1::2] = ['#']*len(line)*2
    else:
        grid[i][::4] = ['#']*(len(line)+1)
for i, j in enumerate(range(2, width, 4)):
    grid[2][j] = line[i]
for i in range(10, width, 12):
    grid[0][i] = '*'
    grid[1][i+1] = '*'
    grid[1][i-1] = '*'
    grid[2][i+2] = '*'
    grid[2][i-2] = '*'
    grid[3][i+1] = '*'
    grid[3][i-1] = '*'
    grid[4][i] = '*'

for row in grid:
    print(''.join(row))