_, min_price = map(int, input().split())
items = list(map(int, input().split()))
items = sorted(items)
n_marked = 1
for i in range(len(items)-1):
    if items[i] + items[i+1] <= min_price:
        n_marked += 1
print(n_marked)
