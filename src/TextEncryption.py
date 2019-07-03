while True:
    n = int(input())
    if n == 0:
        break
    line = input()
    line = list(line.replace(' ', '').upper())
    result = ['.'] * len(line)
    result[0] = line[0]
    first_available = 1

    ind = 0
    for c in line[1:]:
        ind += n
        if ind < len(result):
            result[ind] = c
        else:
            ind = first_available
            result[ind] = c
            first_available += 1
    print(''.join(result))
