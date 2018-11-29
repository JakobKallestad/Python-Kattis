input()
seeds = list(map(int, input().split()))
seeds.sort(reverse=1)
longest_seed = 0
for i, s in enumerate(seeds):
    longest_seed -= 1
    if s > longest_seed:
        longest_seed = s
print(len(seeds) + longest_seed + 1)