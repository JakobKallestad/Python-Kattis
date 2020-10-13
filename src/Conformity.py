from collections import defaultdict

n = int(input())
frosh = defaultdict(int)
for _ in range(n):
    frosh[frozenset(map(int, input().split()))] += 1
frosh = sorted(frosh.values(), reverse=True)
total = 0
i = 0
while i < len(frosh) and frosh[i] == frosh[0]:
    total += frosh[i]
    i += 1
print(total)
