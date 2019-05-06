n_platforms = int(input())
all = [[0] for _ in range(10000)]
starts = []
ends = []
for _ in range(n_platforms):
    h, start, end = map(int, input().split())
    for i in range(start, end):
        all[i].append(h)
    starts.append((start, h))
    ends.append((end-1, h))

starts = sorted(starts, key=lambda x: x[0])
st = 0
ends = sorted(ends, key=lambda x: x[0])
en = 0
total = 0
for x in range(0, 10000):
    all[x] = sorted(all[x], reverse=True)

while st < len(starts):
    for hai in all[starts[st][0]]:
        if hai < starts[st][1]:
            total += starts[st][1]-hai
            break
    st += 1

while en < len(ends):
    for hai in all[ends[en][0]]:
        if hai < ends[en][1]:
            total += ends[en][1]-hai
            break
    en += 1

print(total)
