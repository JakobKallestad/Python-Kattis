from collections import defaultdict

rolls = defaultdict(int)
n, m = map(int, input().split())
for i in range(1, n+1):
    for j in range(1, m+1):
        rolls[i+j] += 1

rolls = sorted(rolls.items(), key=lambda x: -x[1])
best = rolls[0][1]
for ro in rolls:
    if ro[1] != best:
        break
    print(ro[0])
