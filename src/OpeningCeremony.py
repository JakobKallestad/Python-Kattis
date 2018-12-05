from collections import Counter
blocks = int(input())
buildings = list(map(int, input().split()))
buildings.sort(reverse=True)
count, ci, mod = 0, 0, 0
counter = Counter(buildings)

while blocks > 0:
    count += 1
    if buildings[ci]-mod >= blocks:
        blocks -= 1
        ci += 1
    else:
        mod += 1
        blocks -= counter[mod]
print(count)
