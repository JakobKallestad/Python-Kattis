n_socks, cap, max_diff = map(int, input().split())
socks = list(map(int, input().split()))
socks = sorted(socks)

ci = 0
count_machines = 0
while ci < len(socks):
    count_machines += 1
    low_value = socks[ci]
    ci += 1
    in_current_machine = 1
    while ci < len(socks) and in_current_machine < cap:
        if (socks[ci] - low_value) <= max_diff:
            in_current_machine += 1
            ci += 1
        else:
            break

print(count_machines)



'''
Difficult test case:
_ 2 1
1 3 4 5 6 7


'''