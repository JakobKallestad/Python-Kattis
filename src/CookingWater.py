n_logs = int(input())
logs = []
possible = True
for _ in range(n_logs):
    start, end = map(int, input().split())
    logs.append((start, end))
first_ended = min(logs, key=lambda x: x[1])
last_started = max(logs, key=lambda x: x[0])

#print(first_ended)
#print(last_started)

print("edward is right") if last_started[0] > first_ended[1] else print("gunilla has a point")