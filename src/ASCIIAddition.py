def char_to_c(char):
    c = ''
    if char == ['....x', '....x', '....x', '....x', '....x', '....x', '....x']:
        c = '1'
    if char == ['xxxxx', '....x', '....x', 'xxxxx', 'x....', 'x....', 'xxxxx']:
        c = '2'
    if char == ['xxxxx', '....x', '....x', 'xxxxx', '....x', '....x', 'xxxxx']:
        c = '3'
    if char == ['x...x', 'x...x', 'x...x', 'xxxxx', '....x', '....x', '....x']:
        c = '4'
    if char == ['xxxxx', 'x....', 'x....', 'xxxxx', '....x', '....x', 'xxxxx']:
        c = '5'
    if char == ['xxxxx', 'x....', 'x....', 'xxxxx', 'x...x', 'x...x', 'xxxxx']:
        c = '6'
    if char == ['xxxxx', '....x', '....x', '....x', '....x', '....x', '....x']:
        c = '7'
    if char == ['xxxxx', 'x...x', 'x...x', 'xxxxx', 'x...x', 'x...x', 'xxxxx']:
        c = '8'
    if char == ['xxxxx', 'x...x', 'x...x', 'xxxxx', '....x', '....x', 'xxxxx']:
        c = '9'
    if char == ['xxxxx', 'x...x', 'x...x', 'x...x', 'x...x', 'x...x', 'xxxxx']:
        c = '0'
    if char == ['.....', '..x..', '..x..', 'xxxxx', '..x..', '..x..', '.....']:
        c = '+'
    return c


def c_to_char(c):
    char = []
    if c == '1':
        char = ['....x', '....x', '....x', '....x', '....x', '....x', '....x']
    if c == '2':
        char = ['xxxxx', '....x', '....x', 'xxxxx', 'x....', 'x....', 'xxxxx']
    if c == '3':
        char = ['xxxxx', '....x', '....x', 'xxxxx', '....x', '....x', 'xxxxx']
    if c == '4':
        char = ['x...x', 'x...x', 'x...x', 'xxxxx', '....x', '....x', '....x']
    if c == '5':
        char = ['xxxxx', 'x....', 'x....', 'xxxxx', '....x', '....x', 'xxxxx']
    if c == '6':
        char = ['xxxxx', 'x....', 'x....', 'xxxxx', 'x...x', 'x...x', 'xxxxx']
    if c == '7':
        char = ['xxxxx', '....x', '....x', '....x', '....x', '....x', '....x']
    if c == '8':
        char = ['xxxxx', 'x...x', 'x...x', 'xxxxx', 'x...x', 'x...x', 'xxxxx']
    if c == '9':
        char = ['xxxxx', 'x...x', 'x...x', 'xxxxx', '....x', '....x', 'xxxxx']
    if c == '0':
        char = ['xxxxx', 'x...x', 'x...x', 'x...x', 'x...x', 'x...x', 'xxxxx']
    if c == '+':
        char = ['.....', '..x..', '..x..', 'xxxxx', '..x..', '..x..', '.....']
    return char


lines = []
a = []
b = []
plus = False
for _ in range(7):
    lines.append(input())

for i in range(0, len(lines[0]), 6):
    char = []
    for j in range(7):
        char.append(lines[j][i:i+5])
    c = char_to_c(char)
    if c == '+':
        plus = True
    elif not plus:
        a.append(c)
    else:
        b.append(c)

a_num = int(''.join(a))
b_num = int(''.join(b))
total = str(a_num+b_num)
output_length = len(str(total))*6-1

num = [['.' for _ in range(output_length)] for _ in range(7)] # output not modified

# modifying output one char at a time until ready to print
for w, i in enumerate(range(0, output_length, 6)):
    c = total[w]
    char = c_to_char(c)
    for j in range(7):
        num[j][i:i+5] = char[j]

for row in num:
    print(''.join(row))