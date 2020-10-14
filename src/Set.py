from itertools import combinations

cards = []
count = 1
for _ in range(4):
    row = input().split()
    for r in row:
        cards.append(str(count)+r)
        count += 1
triplets = combinations(cards, 3)

exist_set = False
for t in triplets:
    if all(t[0][-i] == t[1][-i] == t[2][-i] or len({t[0][-i], t[1][-i], t[2][-i]}) == 3 for i in range(1, 5)):
        print(*sorted(map(int, [t[0][:-4], t[1][:-4], t[2][:-4]])))
        exist_set = True
if not exist_set:
    print("no sets")

