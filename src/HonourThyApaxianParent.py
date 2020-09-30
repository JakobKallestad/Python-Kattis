y, p = input().split()
if y[-2:] == "ex":
    print(y+p)
elif y[-1] in ('a', 'e', 'i', 'o', 'u'):
    print(y[:-1]+"ex"+p)
else:
    print(y+"ex"+p)
