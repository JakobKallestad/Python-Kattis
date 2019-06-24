from collections import defaultdict

n, h, l = map(int, input().split())
current = list(map(int, input().split()))
next_movies = []
score = {i: float('inf') for i in range(n)}
similar = defaultdict(list)
for c in current:
    score[c] = 0
for _ in range(l):
    a, b = map(int, input().split())
    similar[a].append(b)
    similar[b].append(a)

while True:
    for c in current:
        for f in similar[c]:
            if score[f] == float('inf'):
                score[f] = score[c] + 1
                next_movies.append(f)
    if next_movies == current:
        break
    current = next_movies.copy()

score = sorted(score.items(), key=lambda x: -x[1])
print(score[0][0])
