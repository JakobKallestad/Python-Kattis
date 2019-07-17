n_cars = int(input())
cars = []
for _ in range(n_cars):
    cars.append(int(input()))
liss = [[1, None, None]]*n_cars
for p in range(n_cars):
    liss[p] = [1, cars[p], cars[p]]

i = 0
j = 1
while j < n_cars:
    while i < j:
        if liss[j][0] <= liss[i][0]+1:
            if cars[j] > liss[i][2]:
                liss[j] = [liss[i][0]+1, liss[i][1], cars[j]]
            elif cars[j] < liss[i][1]:
                liss[j] = [liss[i][0]+1, cars[j], liss[i][2]]
        i += 1
    j += 1
    i = 0

result = max(liss, key=lambda x: x[0])[0]
print(result)


'''
7
4
5
1
3
2
8
10
'''

# Still too slow, doesn't work
