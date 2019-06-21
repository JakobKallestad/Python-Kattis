import math

a, b, h = map(int, input().split())
slope = a - b
target = h - a
climbs = math.ceil(target / slope)
print(1 + climbs) if h > a else print(1)
