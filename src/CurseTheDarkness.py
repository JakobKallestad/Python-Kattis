import math

test_cases = int(input())
for _ in range(test_cases):
    x, y = map(float, input().split())
    light = False
    n_candles = int(input())
    for _ in range(n_candles):
        light_x, light_y = map(float, input().split())
        dist_x, dist_y = abs(light_x-x), abs(light_y-y)
        if math.sqrt(dist_x**2 + dist_y**2) <= 8:
            light = True
    if light:
        print("light a candle")
    else:
        print("curse the darkness")