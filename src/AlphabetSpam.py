line = input()

white = 0
lower = 0
upper = 0
symbol = 0

for c in line:
    if ord(c) == 95:
        white += 1
    elif 96 < ord(c) < 123:
        lower += 1
    elif 64 < ord(c) < 91:
        upper += 1
    else:
        symbol += 1

print(white/len(line))
print(lower/len(line))
print(upper/len(line))
print(symbol/len(line))