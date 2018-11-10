from math import sqrt

n = int(input())
for i in range(n):
    line = input()
    decode_list = []
    side = int(sqrt(len(line)))
    for i in range(side):
        for c in range(side-1-i,len(line), side):
            decode_list.append(line[c])
    print(''.join(decode_list))
