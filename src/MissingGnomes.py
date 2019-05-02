n, m = map(int, input().split())
gnome_list = []
used = set()
missing = []
for _ in range(m):
    v = int(input())
    used.add(v)
    gnome_list.append(v)

for i in range(1, n+1):
    if i not in used:
        missing.append(i)

fixed_list = []
i = 0
j = 0
while i < len(gnome_list) or j < len(missing):
    if i >= len(gnome_list):
        fixed_list.append(missing[j])
        j += 1

    elif j >= len(missing):
        fixed_list.append(gnome_list[i])
        i += 1

    elif gnome_list[i] < missing[j]:
        fixed_list.append(gnome_list[i])
        i += 1
    else:
        fixed_list.append(missing[j])
        j += 1

for num in fixed_list:
    print(num)