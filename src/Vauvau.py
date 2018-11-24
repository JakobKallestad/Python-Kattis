def attacked(i, ij, t):
    result = t % ij
    if result == 0:
        return False
    elif result <= i:
        return True
    else:
        return False


def how_many(a, ab, c, cd, x):
    if attacked(a, ab, x) and attacked(c, cd, x):
        print("both")
    elif attacked(a, ab, x) or attacked(c, cd, x):
        print("one")
    else:
        print("none")


a, b, c, d = map(int, input().split())
pmg = list(map(int, input().split()))
ab = a + b
cd = c + d

for x in pmg:
    how_many(a, ab, c, cd, x)
