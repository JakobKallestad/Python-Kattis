n = int(input())

char_to_press = {'a': 2, 'b': 22, 'c': 222, 'd': 3, 'e': 33, 'f': 333, 'g': 4, 'h': 44, 'i': 444, 'j': 5, 'k': 55,
                 'l': 555, 'm': 6, 'n': 66, 'o': 666, 'p': 7, 'q': 77, 'r': 777, 's': 7777, 't': 8, 'u': 88, 'v': 888,
                 'w': 9, 'x': 99, 'y': 999, 'z': 9999, ' ': 0}

for i in range(1, n+1):
    print("Case #{}:".format(i), end=' ')
    line = input()
    pressed = []
    prev = None
    for c in line:
        if prev is not None and char_to_press[c] % 10 == char_to_press[prev] % 10:
            pressed.append(" ")
        pressed.append(char_to_press[c])
        prev = c
    print(''.join([str(c) for c in pressed]))
