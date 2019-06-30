from math import sqrt


def direction(x1, y1, x2, y2, x3, y3):
    val = (y3 - y1) * (x2 - x1) >= (y2 - y1) * (x3 - x1)
    if val == 0:
        return 0 #colinear
    elif val < 0:
        return 1 #anticlockwise
    else:
        return 2 #clockwise


def perpendicular_intersection_distance(x1, y1, x2, y2, x3, y3):
    try:
        k = ((y2 - y1) * (x3 - x1) - (x2 - x1) * (y3 - y1)) / ((y2 - y1)**2 + (x2 - x1)**2)
    except:
        k = 0
    x4 = x3 - k * (y2 - y1)
    y4 = y3 + k * (x2 - x1)
    if is_point_on_line(x1, y1, x2, y2, x4, y4):
        return sqrt((x3-x4)**2+(y3-y4)**2)
    else:
        return float('inf')


def is_point_on_line(x1, y1, x2, y2, x3, y3):
    dist_A = sqrt((x1-x3)**2+(y1-y3)**2)
    dist_B = sqrt((x2-x3)**2+(y2-y3)**2)
    dist_C = sqrt((x1-x2)**2+(y1-y2)**2)
    return round(dist_A + dist_B, 7) == round(dist_C, 7)


def is_intersecting(x1, y1, x2, y2, x3, y3, x4, y4):
    dir1 = direction(x1, y1, x2, y2, x3, y3)
    dir2 = direction(x1, y1, x2, y2, x4, y4)
    dir3 = direction(x3, y3, x4, y4, x1, y1)
    dir4 = direction(x3, y3, x4, y4, x2, y2)

    if dir1 != dir2 and dir3 != dir4:
        return True

    if dir1 == 0 and is_point_on_line(x1, y1, x2, y2, x3, y3): # when p2 of line2 are on the line1
        return True

    if dir2 == 0 and is_point_on_line(x1, y1, x2, y2, x4, y4): # when p1 of line2 are on the line1
        return True

    if dir3 == 0 and is_point_on_line(x3, y3, x4, y4, x1, y1): # when p2 of line1 are on the line2
        return True

    if dir4 == 0 and is_point_on_line(x3, y3, x4, y4, x2, y2): # when p1 of line1 are on the line2
        return True

    return False


n_test_cases = int(input())
for _ in range(n_test_cases):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    if is_intersecting(x1, y1, x2, y2, x3, y3, x4, y4):
        print("0.00")
        continue
    line_one = [(x1, y1), (x2, y2)]
    line_two = [(x3, y3), (x4, y4)]
    distances = []
    # Distance between points
    for p1 in line_one:
        for p2 in line_two:
            dist = sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
            distances.append(dist)
    # Perpendicular distances:
    for p in line_one:
        distances.append(perpendicular_intersection_distance(*line_two[0], *line_two[1], *p))
    for p in line_two:
        distances.append(perpendicular_intersection_distance(*line_one[0], *line_one[1], *p))
    print("{:.2f}".format(min(distances)))
