n_cups = int(input())
cups = []
for _ in range(n_cups):
    a, b = input().split()
    try:
        a = int(a)
        cups.append((b, a))
    except:
        b = int(b)
        cups.append((a, b*2))

cups = sorted(cups, key=lambda x: x[1])
for cu in cups:
    print(cu[0])
