n_teams, n_damaged, n_reserves = map(int, input().split())
damaged = set(map(int, input().split()))
reserves = set(map(int, input().split()))
can_not_attend = len(damaged)

helps_themselves = damaged.intersection(reserves)
damaged = damaged.difference(helps_themselves)
reserves = reserves.difference(helps_themselves)
reserves = sorted(reserves)
can_not_attend -= len(helps_themselves)

for r in reserves:
    if r-1 in damaged:
        can_not_attend -= 1
        damaged.remove(r-1)
    elif r+1 in damaged:
        can_not_attend -= 1
        damaged.remove(r+1)
print(can_not_attend)
