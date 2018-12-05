d = {}
e = {}

n = int(input())
runners = []
for _ in range(n):
    name, first, second = map(str, input().split())
    runners.append((name, first, second))
    d[name] = float(second)
    e[name] = float(first)

name_list = sorted(d, key=lambda x: d[x])
best_first = sorted(runners, key=lambda x: x[1])
best_second = sorted(runners, key=lambda x: x[2])


best_time = float('inf')
best_team = []

for starter in name_list:
    current_time = e[starter]
    current_team = [starter]
    for ender in name_list:
        if starter == ender:
            continue
        current_time += d[ender]
        current_team.append(ender)
        if len(current_team) == 4:
            break
    if current_time < best_time:
        best_time = current_time
        best_team = current_team

print("{:.9f}".format(best_time))
print('\n'.join(best_team))
