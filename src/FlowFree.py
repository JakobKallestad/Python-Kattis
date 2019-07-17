import sys

grid = [list(input()) for _ in range(4)]
red = []
green = []
blue = []
yellow = []
visited = [[False]*4 for _ in range(4)]
vCount = 0
for y in range(4):
    for x in range(4):
        if grid[y][x] == 'R':
            red.append((y, x))
            visited[y][x] = True
        elif grid[y][x] == 'G':
            green.append((y, x))
            visited[y][x] = True
        elif grid[y][x] == 'B':
            blue.append((y, x))
            visited[y][x] = True
        elif grid[y][x] == 'Y':
            yellow.append((y, x))
            visited[y][x] = True


def dfs(cy, cx, ty, tx, level, searches, t_length, visited, vCount):
    visited[cy][cx] = True
    vCount += 1

    if (cy, cx) == (ty, tx):
        if level + 1 == t_length:
            if vCount == 16:
                print("solvable")
                sys.exit()
        else:
            level += 1
            ny, nx = searches[level][0]
            nty, ntx = searches[level][1]
            dfs(ny, nx, nty, ntx, level, searches, t_length, visited, vCount)

    else:
        # North:
        if cy - 1 >= 0 and not visited[cy - 1][cx] or (cy-1, cx) == (ty, tx):
            dfs(cy - 1, cx, ty, tx, level, searches, t_length, visited, vCount)

        # East:
        if cx + 1 < 4 and not visited[cy][cx + 1] or (cy, cx+1) == (ty, tx):
            dfs(cy, cx + 1, ty, tx, level, searches, t_length, visited, vCount)

        # South:
        if cy + 1 < 4 and not visited[cy + 1][cx] or (cy+1, cx) == (ty, tx):
            dfs(cy + 1, cx, ty, tx, level, searches, t_length, visited, vCount)

        # West:
        if cx - 1 >= 0 and not visited[cy][cx - 1] or (cy, cx-1) == (ty, tx):
            dfs(cy, cx - 1, ty, tx, level, searches, t_length, visited, vCount)

        if grid[cy][cx] == 'W':
            visited[cy][cx] = False
    vCount -= 1


searches = [red, green, blue]
if yellow:
    searches.append(yellow)
dfs(*red[0], *red[1], 0, searches, len(searches), visited, vCount)
print("not solvable")

'''
RGBW
YWWW
RGBW
YWWW
'''

'''
RGBW
WWWW
WWWW
RGBW
'''

'''
RWRG
GWWW
BBWW
WWYY
'''

'''
RGBY
WWWW
WWWW
RGYB
'''

# worst one
'''
RBGW
WWWW
WWWW
BRWG
'''
