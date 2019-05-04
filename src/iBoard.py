while True:
    try:
        line = list(input())
        line = [format(ord(x), 'b') if len(format(ord(x), 'b')) == 7 else '0' + format(ord(x), 'b') for x in line]
        line = ' '.join(map(str, line))

        if line.count('0') % 2 == 0 and line.count('1') % 2 == 0:
            print("free")
        else:
            print("trapped")
    except EOFError:
        break
