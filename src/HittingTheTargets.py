n_targets = int(input())
targets = []
for _ in range(n_targets):
    info = input().split()
    if info[0] == "rectangle":
        x1, y1, x2, y2 = map(int, info[1:])
        targets.append((x1, y1, x2, y2))
    else:
        x, y, r = map(int, info[1:])
        targets.append((x, y, r))

n_shots = int(input())
for _ in range(n_shots):
    count = 0
    x, y = map(int, input().split())
    for t in targets:
        if len(t) == 3:
            count += (((x-t[0])**2 + (y-t[1])**2)**0.5 <= t[2])
        else:
            count += (t[0] <= x <= t[2] and t[1] <= y <= t[3])
    print(count)