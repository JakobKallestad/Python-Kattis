range_list = input().split()
start = int(range_list[0])
end = int(range_list[1])

combinations = 0

for i in range(end-start):
    check = start+i
    if check%2 != 0:
        continue
    temp = str(check)
    temp_set = set()
    fail = False
    for c in temp:
        temp_set.add(int(c))
    #print(temp_set)
    if 0 in temp_set:
        continue
    if len(temp_set) != 6:
        continue
    for num in temp_set:
        if check%num != 0:
            fail = True
            break
    if not fail:
        combinations += 1
print(combinations)
