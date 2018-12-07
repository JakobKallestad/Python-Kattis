import math

line = [c for c in input()]
length = len(line)
n_rows, n_cols = 0, 0
for i in range(int(math.sqrt(length)), 0, -1):
    n_rows = i
    n_cols = length//n_rows
    if n_rows*n_cols == length:
        break
decrypted = []
for i in range(n_rows):
    decrypted += line[i::n_rows]
print(''.join(decrypted))
