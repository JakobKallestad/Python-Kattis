cases = int(input())
for i in range(cases):
    #trusted = 0
    #cities = set()
    n, m = map(int, input().split())
    for j in range(m):
        a, b = map(int, input().split())
        #if (a not in cities or b not in cities) and len(cities) < n:
            #cities.add(a)
            #cities.add(b)
            #trusted += 1
    #assert trusted == n-1
    print(n-1)
