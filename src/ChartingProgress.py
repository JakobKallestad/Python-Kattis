from collections import defaultdict


def make_grid():
    try:
        grid = []
        while True:
            line = input()
            if not line:
                break
            grid.append(line)
        return grid
    except EOFError:
        return grid


while True:
    try:
        grid = make_grid()
        height = len(grid)
        width = len(grid[0])
        ast_count = defaultdict(int)
        for i in range(height):
            count_astrics = grid[i].count('*')
            ast_count[i] = count_astrics
        grid = [['.'] * width for _ in range(height)]

        currentX = width - 1
        for i in range(height):
            row = grid[i]
            for _ in range(ast_count[i]):
                row[currentX] = '*'
                currentX -= 1

        for row in grid:
            print(''.join(row))
        print()

    except (EOFError, IndexError):
        break
