import sys

raw_n = input()
n = int(raw_n)
digit_list = [c for c in raw_n]

if raw_n == ''.join(sorted(raw_n))[::-1]:
    print(0)
    sys.exit(0)

current = n+1
while True:
    i = str(current)
    if len(i) != len(raw_n):
        continue

    if sorted(i) == sorted(raw_n):
        print(current)
        break

    current += 1
