n = int(input())
for _ in range(n):
    line = list(input())
    enc = line[0] == 'e'
    line = line[2:]

    first = [ord(c)-96 for c in line]
    first = [0 if i == -64 else i for i in first]
    second = first[:]

    if enc:
        for i in range(1, len(second)):
            second[i] = second[i]+second[i-1]
        third = [i%27 for i in second]

    else:
        for i in range(1, len(second)):
            if first[i] < first[i-1]:
                second[i] = second[i-1]+(27-(first[i-1]-first[i]))
            else:
                second[i] = second[i-1] + first[i]-first[i-1]
        third = [a-b for a, b in zip(second[1:], second)]
        third.insert(0, second[0])

    fourth = [chr(i+96) for i in third]
    fin = [' ' if c == '`' else c for c in fourth]
    print(''.join(fin))
