from collections import deque

n_test_cases = int(input())
for _ in range(n_test_cases):
    n = int(input())
    grid = [list(input()) for _ in range(n)]
    orientation = (1, 2, 3, 4, 5, 6)

    # Move shifts:
    north_order = (3, 1, 0, 5, 4, 2)
    east_order = (4, 0, 2, 3, 5, 1)
    south_order = (2, 1, 5, 0, 4, 3)
    west_order = (1, 5, 2, 3, 0, 4)

    visited = [[set() for _ in range(n)] for _ in range(n)]

    queue = deque()
    end_y, end_x = -1, -1
    for y in range(n):
        for x in range(n):
            if grid[y][x] == 'S':
                visited[y][x].add(orientation)
                queue.append((y, x, orientation))
            elif grid[y][x] == 'H':
                end_y, end_x = y, x

    while queue:
        cy, cx, orientation = queue.popleft()

        # Win condition:
        if (cy, cx) == (end_y, end_x) and orientation[5] == 5:
            print("Yes")
            break

        # North:
        n_orientation = tuple(orientation[i] for i in north_order)
        if cy-1>=0 and n_orientation not in visited[cy-1][cx] and grid[cy-1][cx] != '*':
            visited[cy-1][cx].add(n_orientation)
            queue.append((cy-1, cx, n_orientation))

        # East:
        e_orientation = tuple(orientation[i] for i in east_order)
        if cx+1<n and e_orientation not in visited[cy][cx+1] and grid[cy][cx+1] != '*':
            visited[cy][cx+1].add(e_orientation)
            queue.append((cy, cx+1, e_orientation))

        # South:
        s_orientation = tuple(orientation[i] for i in south_order)
        if cy+1<n and s_orientation not in visited[cy+1][cx] and grid[cy+1][cx] != '*':
            visited[cy+1][cx].add(s_orientation)
            queue.append((cy+1, cx, s_orientation))

        # West:
        w_orientation = tuple(orientation[i] for i in west_order)
        if cx-1>=0 and w_orientation not in visited[cy][cx-1] and grid[cy][cx-1] != '*':
            visited[cy][cx-1].add(w_orientation)
            queue.append((cy, cx-1, w_orientation))
    else:
        print("No")
