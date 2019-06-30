n = int(input())
total = 0
temp = 1
for i in range(1, n+1):
    temp *= i
    total += 1/temp
total += 1

print(total)