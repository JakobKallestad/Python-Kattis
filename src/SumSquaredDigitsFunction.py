n_datasets = int(input())
for i in range(1, n_datasets+1):
    _, b, n = map(int, input().split())
    ssd = 0
    while n:
        ssd += (n%b)**2
        n //= b
    print(i, ssd)

