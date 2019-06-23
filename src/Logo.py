from math import cos, sin, sqrt, pi

n_test_cases = int(input())
for _ in range(n_test_cases):
    current_y, current_x, current_angle = 0, 0, 0
    n_commands = int(input())
    for _ in range(n_commands):
        com, amount = map(str, input().split())
        amount = int(amount)
        if com == "fd":
            current_y += amount*sin(current_angle * (pi / 180))
            current_x += amount*cos(current_angle * (pi / 180))
        elif com == "lt":
            current_angle += amount
        elif com == "rt":
            current_angle -= amount
        else:
            current_y -= amount * sin(current_angle * (pi / 180))
            current_x -= amount * cos(current_angle * (pi / 180))
    dist = round(sqrt(current_y**2 + current_x**2))
    print(dist)
