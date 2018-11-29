def start_xy_dr(x, y):
    if x < y:
        start_x = 0
        start_y = y-x
    else:
        start_y = 0
        start_x = x-y
    return start_x, start_y


def start_xy_dl(x, y):
    if 7-x < y:
        start_x = 7
        start_y = y-(7-x)
    else:
        start_y = 0
        start_x = x+y
    return start_x, start_y


board = []
n_queens = 0
for _ in range(8):
    line = [c for c in input()]
    board.append(line)

all_good = True


for y in range(8):
    for x in range(8):
        if board[y][x] == '*':
            n_queens += 1

            if any('*' == board[y][n] and n != x for n in range(len(board[y][:]))):
                all_good = False
                break
            if any('*' == board[n][x] and n != y for n in range(len(board[:][x]))):
                all_good = False
                break

            start_x, start_y = start_xy_dr(x, y)
            if any('*' == board[n][m] and m != x and n != y for n, m in zip(range(start_y, 8), range(start_x, 8))):
                all_good = False
                break

            start_x, start_y = start_xy_dl(x, y)
            if any('*' == board[n][m] and m != x and n != y for n, m in zip(range(start_y, 8), range(start_x, 0, -1))):
                all_good = False
                break



print("valid") if all_good and n_queens == 8 else print("invalid")

