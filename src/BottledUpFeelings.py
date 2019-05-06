oil, big, small = map(int, input().split())
big_checks = []
small_checks = {}

current = 0
while current <= oil:
    big_checks.append(current)
    current += big

i = 1
current = small
while current <= oil:
    small_checks[current] = i
    current += small
    i += 1

for i in range(len(big_checks)-1, -1, -1):
    if big_checks[i] == oil:
        print(i, 0)
        break
    elif (oil-big_checks[i]) in small_checks:
        print(i, small_checks[oil-big_checks[i]])
        break
else:
    print("Impossible")