_, max_capacity = map(int, input().split())
food = list(map(int, input().split()))
max_eaten = 0
for i in range(len(food)):
    current_belly = 0
    n_eaten = 0
    while i < len(food):
        if current_belly + food[i] <= max_capacity:
            current_belly += food[i]
            n_eaten += 1
        i += 1
    max_eaten = max(max_eaten, n_eaten)
print(max_eaten)
