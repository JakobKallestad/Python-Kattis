n, p, k = map(int, input().split())
p /= 100
speedups = list(map(int, input().split()))
speedups.append(k)
original_time = 0
prev_time = 0
current_increase = 1
for inc in speedups:
    duration = inc - prev_time
    original_time += duration*current_increase
    current_increase += p
    prev_time = inc
print(original_time)


