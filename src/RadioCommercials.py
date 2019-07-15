n, p = map(int, input().split())
commercials = list(map(lambda x: int(x)-p, input().split()))
for i in range(1, n):
    commercials[i] = max(commercials[i], commercials[i-1]+commercials[i])
print(max(commercials))
