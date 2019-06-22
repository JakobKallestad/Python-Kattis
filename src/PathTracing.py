visited = set()
highX, lowX, highY, lowY = 0, 0, 0, 0
current_pos = (0, 0)

while True:
    try:
        dir = input()
        if dir == "up":
            current_pos = (current_pos[0]+1, current_pos[1])
        elif dir == "down":
            current_pos = (current_pos[0]-1, current_pos[1])
        elif dir == "left":
            current_pos = (current_pos[0], current_pos[1]-1)
        else:
            current_pos = (current_pos[0], current_pos[1]+1)
        visited.add(current_pos)

        if current_pos[0] < lowY:
            lowY = current_pos[0]
        if current_pos[0] > highY:
            highY = current_pos[0]
        if current_pos[1] < lowX:
            lowX = current_pos[1]
        if current_pos[1] > highX:
            highX = current_pos[1]

    except EOFError:
        break

# made the grid:
height = highY-lowY+3
width = highX-lowX+3
grid = [[' ']*width for _ in range(height)]

# make the border
grid[0] = ['#']*width
grid[-1] = ['#']*width
for y in range(len(grid)):
    grid[y][0] = '#'
    grid[y][-1] = '#'

# start and end points
startX = width-2 - highX
startY = 1+highY
endY = startY-current_pos[0]
endX = startX+current_pos[1]

# fill in the visited points
for loc in visited:
    grid[startY-loc[0]][startX+loc[1]] = '*'

grid[startY][startX] = 'S'
grid[endY][endX] = 'E'

# display grid
for row in grid:
    print(''.join(row))
