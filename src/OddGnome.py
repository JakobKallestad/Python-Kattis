n = int(input())
for _ in range(n):
    gnomes = list(map(int, input().split()[1:]))
    start = gnomes[0]
    for i in range(0, len(gnomes)):
        if gnomes[i] != start:
            print(i+1)
            break
        start += 1
