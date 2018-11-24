n = int(input())
inc = True
dec = True
prev = None
for _ in range(n):
    line = input()
    if prev is not None:
        if line > prev:
            dec = False
        if line < prev:
            inc = False
    prev = line

if inc:
    print("INCREASING")
elif dec:
    print("DECREASING")
else:
    print("NEITHER")