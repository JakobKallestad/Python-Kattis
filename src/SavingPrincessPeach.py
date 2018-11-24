n, m = map(int, input().split())
observed = set()
for _ in range(m):
    observed.add(int(input()))
for i in range(n):
    if i not in observed:
        print(i)
print("Mario got {seen} of the dangerous obstacles.".format(seen=len(observed)))