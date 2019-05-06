input()
tasks = list(map(int, input().split()))
intervals = list(map(int, input().split()))
tasks = sorted(tasks, reverse=True)
intervals = sorted(intervals, reverse=True)
i = 0
j = 0
n_completed = 0
while i < len(tasks) and j < len(intervals):
    if tasks[i] <= intervals[j]:
        n_completed += 1
        i += 1
        j += 1
    else:
        i += 1

print(n_completed)
