line = input()
l3 = len(line) // 3
one = line[:l3]
two = line[l3:l3*2]
three = line[-l3:]
if one == two:
    print(one)
elif two == three:
    print(two)
else:
    print(one)
