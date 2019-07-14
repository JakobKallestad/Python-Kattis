n, b = map(int, input().split())
total = 1
for i in range(1, b+1):
    total += 2**i
print("yes") if total >= n else print("no")
