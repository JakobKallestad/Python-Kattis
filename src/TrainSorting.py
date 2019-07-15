n_cars = int(input())
cars = []
for _ in range(n_cars):
    cars.append(int(input()))
i = 0
j = 1
liss = [1]*n_cars

while j < n_cars:
    while i < j:
        if cars[i] < cars[j]:
            liss[j] = max(liss[i]+1, liss[j])
        i += 1
    j += 1
    i = 0
print(max(liss))

# This won't work because you can add cars to the end as well
