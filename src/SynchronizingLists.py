while True:
    n = int(input())
    if n == 0:
        break
    list_a = []
    list_b = []
    for i in range(n):
        list_a.append(int(input()))
    for i in range(n):
        list_b.append(int(input()))
    list_a_sorted = sorted(list_a)
    list_b_sorted = sorted(list_b)
    sync_dict = {}
    for a, b in zip(list_a_sorted, list_b_sorted):
        sync_dict[a] = b
    #print(sync_dict)
    for i,a in zip(range(n),list_a):
        print(sync_dict[a])
    print()