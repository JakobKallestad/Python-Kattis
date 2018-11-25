from collections import Counter

line = input()
chars = [c for c in line]
chars = sorted(chars)
dict = Counter(chars)
remove_count = 0
for value in dict.values():
    if value % 2 != 0:
        remove_count += 1
if remove_count != 0:
    remove_count -= 1
print(remove_count)
