n_cities, queries = map(int, input().split())
cities = {n: x for n, x in zip(range(1, n_cities + 1), list(map(int, input().split())))}
for _ in range(queries):
    a, b, c = map(int, input().split())
    if a == 1:
        cities[b] = c
    else:
        print(abs(cities[b] - cities[c]))
