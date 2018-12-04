grid = []
expanded = []
n_words, n_chars = map(int, input().split())
u, l, r, d = map(int, input().split())
width = l+n_chars+r
height = u+n_words+d

for _ in range(n_words):
    grid.append([c for c in input()])

for i in range(height):
    expanded.append(['.']*width)
    if i % 2 == 0:
        expanded[i][::2] = ['#' for n in expanded[i][::2]]
    else:
        expanded[i][1::2] = ['#' for n in expanded[i][1::2]]

for i, y in zip(range(n_words), range(u, u+n_words)):
    for j, x in zip(range(n_chars), range(l, l+n_chars)):
        expanded[y][x] = grid[i][j]

for line in expanded:
    print(''.join(line))
