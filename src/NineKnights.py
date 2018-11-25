import sys

grid = list()
legal_moves = list()
knight_count = 0
for _ in range(5):
    grid.append([c for c in input()])
    legal_moves.append([True for _ in range(5)])

for y in range(len(grid)):
    for x in range(len(grid[y])):

        # adds illegal moves
        if grid[y][x] == 'k':
            knight_count += 1

            # found collision
            if not legal_moves[y][x]:
                print("invalid")
                sys.exit()

            # no more illegal moves introduced
            if y == 4:
                continue

            # add new illegal moves
            if x >= 2:
                legal_moves[y+1][x-2] = False
            if x <= 2:
                legal_moves[y+1][x+2] = False
            if y <= 2:
                if x > 0:
                    legal_moves[y+2][x-1] = False
                if x < 4:
                    legal_moves[y+2][x+1] = False

print("valid") if knight_count == 9 else print("invalid")