n = int(input())
for _ in range(n):
    turtles = list(map(int, input().split()[:-1]))
    prev = turtles[0]
    imported = 0
    for t in turtles:
        if prev*2 < t:
            imported += t-prev*2
        prev = t
    print(imported)