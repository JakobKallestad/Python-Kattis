n = int(input())
for i in range(n):
    print("Test", i+1)
    r, c = map(int, input().split())
    grid = []
    for _ in range(r):
        grid.append(input()[::-1])
    grid = list(reversed(grid))
    for line in grid:
        print(line)