import math
b, br, bs, a, ass = map(int, input().split())
bob_money = (br-b)*bs
ar = math.floor(a+bob_money/ass)+1
print(ar)
