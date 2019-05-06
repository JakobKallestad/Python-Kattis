chars = {i:chr(i+96) for i in range(1, 27)}
l, w = map(int, input().split())
output = []
if l <= w <= l*26:
    while w-26 >= l-1:
        w -= 26
        l -= 1
        output.append('z')
    if w > 0:
        l -= 1
        output.append(chars[w-l])
        while l > 0:
            output.append('a')
            l -= 1
    print(''.join(output))
else:
    print("impossible")
