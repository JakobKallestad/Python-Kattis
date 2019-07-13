from collections import deque

n_researchers, n_locktime = map(int, input().split())
events = []
savings = 0
empty_queue = deque()
for _ in range(n_researchers):
    a, s = map(int, input().split())
    done_time = a+s
    events.append((a, 1))
    events.append((done_time, 0))
events = sorted(events)

for e in events:
    if e[1] == 1:
        while empty_queue:
            work_station = empty_queue.popleft()
            if e[0] - work_station[0] <= n_locktime:
                savings += 1
                break
    else:
        empty_queue.append(e)
print(savings)
