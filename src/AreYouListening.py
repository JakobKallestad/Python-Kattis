import math

x, y, n_devices = map(int, input().split())
devices = []
for _ in range(n_devices):
    devices.append(tuple(map(int, input().split())))
close_devices = sorted(devices, key=lambda dev:math.sqrt((x-dev[0])**2 + (y-dev[1])**2)-dev[2])
dev = close_devices[2]
dist = math.sqrt((x - dev[0]) ** 2 + (y - dev[1]) ** 2) - dev[2]
print(math.floor(dist)) if dist > 0 else print(0)
