k = int(input())
count = 1
current = 0
for _ in range(k):
    new = int(input())
    if new < current:
        count += 1
    current = new
print(count)