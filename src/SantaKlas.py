import math

height, angle = map(int, input().split())
if angle <= 180:
    print("safe")
else:
    top_angle = 360 - (angle + 90)
    bot_angle = 180 - (top_angle + 90)
    c = height / math.sin(math.radians(bot_angle))
    print(math.floor(c))
