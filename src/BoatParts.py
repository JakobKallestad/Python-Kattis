p, n = map(int, input().split())
boat_set = set()
count = 0
for i in range(n):
    part = input()
    if len(boat_set) == p:
        count = i
    boat_set.add(part)
if len(boat_set) == p:
    print(count)
else:
    print("paradox avoided")
