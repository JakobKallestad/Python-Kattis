n = int(input())
count = 0
for _ in range(n):
    line = input().lower()
    if "pink" in line or "rose" in line:
        count += 1
print(count) if count > 0 else print("I must watch Star Wars with my daughter")