l, n = map(int, input().split())
count = 1
while l % n > 0:
    n -= l % n
    count += 1
print(count)

