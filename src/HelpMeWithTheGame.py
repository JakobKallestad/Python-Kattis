def order_pieces(color, is_black):
    p_values = {'K': 1, 'Q': 2, 'R': 3, 'B': 4, 'N': 5, 'P': 6}
    color = sorted(color, key=lambda x: x[1])
    color = sorted(color, key=lambda x: x[2], reverse=is_black)
    color = sorted(color, key=lambda x: p_values[x[0]])
    return color


def notation(color):
    fin = []
    for p in color:
        if p[0] == 'P':
            fin.append(''.join(map(str, p[1:])))
        else:
            fin.append(''.join(map(str, p)))
    return ','.join(fin)


grid = []
for i in range(17):
    grid.append(list(input()))

white = []
black = []

for i, j in zip(range(8, 0, -1), range(1, 17, 2)):  # rows
    for k, l in zip(range(8), range(2, 33, 4)):  # cols
        c = grid[j][l]
        if 64 < ord(c) < 91:
            p_info = (c, chr(97 + k), i)
            white.append(p_info)
        elif 96 < ord(c) < 123:
            p_info = (c.upper(), chr(97 + k), i)
            black.append(p_info)

white = order_pieces(white, False)
black = order_pieces(black, True)
print("White:", notation(white))
print("Black:", notation(black))
