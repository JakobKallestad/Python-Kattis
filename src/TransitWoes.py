s, t, n = map(int, input().split())
walk_times = list(map(int, input().split()))
transit_times = list(map(int, input().split()))
buss_arrivals = list(map(int, input().split()))
current_time = s+walk_times[0]

for wa, tr, bu in zip(walk_times[1:], transit_times, buss_arrivals):
    current_time += (bu - current_time%bu)%bu
    current_time += tr
    current_time += wa
print("yes") if current_time <= t else print("no")