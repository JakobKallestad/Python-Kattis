grid = [[] for _ in range(17)]


def insert_pieces(color, low):
    for p in color:
        cor_start = 1
        if len(p) == 3:
            symbol = p[0]
        else:
            symbol = 'P'
            cor_start = 0
        if low:
            symbol = symbol.lower()
        y = 17 - int(p[cor_start+1]) * 2
        x = (ord(p[cor_start]) - 97) * 4 + 2
        grid[y][x] = symbol


for i in range(0, 17, 1):
    if i % 2 == 0:
        grid[i] = ['+', '-', '-', '-'] * 8 + ['+']
    elif (i - 1) % 4 == 0:
        grid[i] = ['|', '.', '.', '.', '|', ':', ':', ':'] * 4 + ['|']
    else:
        grid[i] = ['|', ':', ':', ':', '|', '.', '.', '.'] * 4 + ['|']

white = input()
black = input()
if len(white) > 7:
    white = white[7:].split(',')
else:
    white = []
if len(black) > 7:
    black = black[7:].split(',')
else:
    black = []

insert_pieces(white, False)
insert_pieces(black, True)
for row in grid:
    print(''.join(row))

