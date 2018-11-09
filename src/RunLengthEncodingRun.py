inp = input().split()
mode = inp[0]
line = inp[1]
fin_list = []
current_char = line[0]
count_current = 0


if mode == 'E':
    for c in line:
        if c == current_char:
            count_current += 1
        else:
            fin_list.append(current_char)
            fin_list.append(str(count_current))
            current_char = c
            count_current = 1
    fin_list.append(current_char)
    fin_list.append(str(count_current))
else:
    for i in range(0, (len(line)-1), 2):
        fin_list.append(line[i]*int(line[i+1]))

print(''.join(fin_list))