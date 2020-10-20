s = input()
p = input()
if s == p or (p == s[1:] and s[0].isdigit()) or (p == s[:-1] and s[-1].isdigit()) or (p.swapcase() == s):
    print("YES")
else:
    print("NO")