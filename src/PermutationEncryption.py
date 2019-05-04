from math import ceil

while True:
    key = list(map(int, input().split()))
    if key[0] == 0:
        break
    key = key[1:]
    line = list(input())
    l_line, l_key = len(line), len(key)
    key = key * ceil(l_line/l_key)

    encrypted = []
    section = -l_key
    for i in range(len(key)):
        if i % l_key == 0:
            section += l_key
        shift = key[i]
        look = shift-1+section
        if look < l_line:
            c = line[look]
        else:
            c = ' '
        encrypted.append(c)
    print("'"+''.join(encrypted)+"'")

'''
6 4 1 3 5 2 6
Four score and seven years ago.
'''
