total_capacity, n_stations = map(int, input().split())
current_passengers = 0
for _ in range(n_stations):
    left, entered, stayed = map(int, input().split())
    after_left = current_passengers-left
    if after_left < 0:
        print("impossible")
        break
    if after_left + entered > total_capacity:
        print("impossible")
        break
    if after_left + entered < total_capacity and stayed > 0:
        print("impossible")
        break
    current_passengers += (entered-left)
else:
    print("possible") if current_passengers == 0 else print("impossible")