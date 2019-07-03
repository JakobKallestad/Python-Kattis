# Annoyingly could NOT pass this task. I would have liked a more clarifying task description. I have tried most things,
# that I can interpret the description to mean, but there probably is some silly mistake.

from collections import defaultdict

rank_to_points = defaultdict(lambda: 0)
rank_to_points.update({
    1: 100,
    2: 75,
    3: 60,
    4: 50,
    5: 45,
    6: 40,
    7: 36,
    8: 32,
    9: 29,
    10: 26,
    11: 24,
    12: 22,
    13: 20,
    14: 18,
    15: 16,
    16: 15,
    17: 14,
    18: 13,
    19: 12,
    20: 11,
    21: 10,
    22: 9,
    23: 8,
    24: 7,
    25: 6,
    26: 5,
    27: 4,
    28: 3,
    29: 2,
    30: 1
})
contestant_to_score = {}

n_contestants = int(input())
contestants = []
for _ in range(n_contestants):
    contestants.append(tuple(map(int, input().split())))

sorted_contestants = sorted(contestants, key=lambda tup: tup[2])
sorted_contestants = sorted(sorted_contestants, key=lambda tup: tup[1])
sorted_contestants = sorted(sorted_contestants, key=lambda tup: -tup[0])

ind = 0
cur_rank = 1
while ind < len(sorted_contestants):
    if sorted_contestants[ind][:-1] == (0, 0, 0):
        contestant_to_score[sorted_contestants[ind]] = sorted_contestants[ind][-1]
        ind += 1
        cur_rank += 1
        continue
    extra = 1
    while ind+extra < len(sorted_contestants) and sorted_contestants[ind][:-1] == sorted_contestants[ind+extra][:-1]:
        extra += 1

    if extra > 1:
        for i in range(extra):
            contestant_to_score[sorted_contestants[ind+i]] = rank_to_points[cur_rank] + sorted_contestants[ind+i][-1]
        ind += extra
        cur_rank += extra
    else:
        contestant_to_score[sorted_contestants[ind]] = rank_to_points[cur_rank] + sorted_contestants[ind][-1]
        ind += 1
        cur_rank += 1

for con in contestants:
    print(contestant_to_score[con])
