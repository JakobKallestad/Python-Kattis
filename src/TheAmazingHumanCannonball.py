from math import cos, sin, radians

n_test_cases = int(input())
for _ in range(n_test_cases):
    v0, angle, x1, h1, h2 = map(float, input().split())
    critical_time = x1 / (v0 * cos(radians(angle)))
    h3 = v0*critical_time*sin(radians(angle))-(1/2)*9.81*critical_time**2
    if h3-1 > h1 and h3+1 < h2:
        print("Safe")
    else:
        print("Not Safe")
