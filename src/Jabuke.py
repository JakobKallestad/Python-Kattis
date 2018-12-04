def area(x1, y1, x2, y2, x3, y3):
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2


def isInside(x1, y1, x2, y2, x3, y3, x, y, area_anta):
    A = area_anta
    A1 = area(x, y, x2, y2, x3, y3)
    A2 = area(x1, y1, x, y, x3, y3)
    A3 = area(x1, y1, x2, y2, x, y)
    return A == A1 + A2 + A3


xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())
area_anta = abs(xa * (yb - yc) + xb * (yc - ya) + xc * (ya - yb)) / 2
print("{:0.1f}".format(area_anta))

count = 0
n_trees = int(input())
for _ in range(n_trees):
    xd, yd = map(int, input().split())
    if isInside(xa, ya, xb, yb, xc, yc, xd, yd, area_anta):
        count += 1
print(count)
