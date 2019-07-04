emma = list(map(int, input().split()))[1:]
marcos = list(map(int, input().split()))[1:]
emma_b = [False]*1000000
marcos_b = [False]*1000000

for e in emma:
    emma_b[e] = True
for m in marcos:
    marcos_b[m] = True

count_together = 0
emma_dibs = False
marcos_dibs = False
for d in range(1000000):
    if emma_b[d]:
        if marcos_b[d]:
            count_together += 1
            emma_dibs = False
            marcos_dibs = False
        elif not marcos_dibs:
            count_together += 1
            emma_dibs = False
            marcos_dibs = True
    elif marcos_b[d] and not emma_dibs:
        count_together += 1
        emma_dibs = True
        marcos_dibs = False

print(count_together)
