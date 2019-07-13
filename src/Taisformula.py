n_points = int(input())
points = []
for _ in range(n_points):
    x, y = map(float, input().split())
    points.append((x, y))
points.append((points[-1][0], 0))
points.append((points[0][0], 0))
area = 0.0
for i in range(n_points+2):
    j = (i + 1) % (n_points+2)
    area += points[i][0] * points[j][1]
    area -= points[j][0] * points[i][1]
area = abs(area) / 2000.0
print(area)
