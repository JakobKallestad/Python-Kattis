from collections import Counter

group_size = int(input())
group = list(map(int, input().split()))
counter = Counter
gc = list(counter(group).items())
gc = sorted(gc, key=lambda x: x[0], reverse=True)
gc = sorted(gc, key=lambda x: x[1])

if gc[0][1] != 1:
    print("none")
else:
    print(group.index(gc[0][0]) + 1)
