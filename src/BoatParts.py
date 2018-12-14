p, n = map(int, input().split())
boat_set = set()
last_working_day = 0
for i in range(1, n+1):
    part = input()
    boat_set.add(part)
    if len(boat_set) == p:
        last_working_day = i
        break
print(last_working_day) if len(boat_set) == p else print("paradox avoided")

