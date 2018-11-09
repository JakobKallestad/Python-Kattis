from collections import Counter
n = int(input())
for i in range(n):
    n_guests = int(input())
    guest_list = list(map(int, input().split()))
    c = Counter(guest_list)
    alone = c.most_common()[-1][0]
    print("Case #{}: {}".format(i+1,alone))

