n = int(input())
grid = [input() for _ in range(n)]
grid_T = list(map(''.join, zip(*grid)))
for line, line_T in zip(grid, grid_T):
    if "WWW" in line or "BBB" in line or "WWW" in line_T or "BBB" in line_T:
        print(0)
        break
    elif line.count("W") != line.count("B") or line_T.count("W") != line_T.count("B"):
        print(0)
        break
else:
    print(1)