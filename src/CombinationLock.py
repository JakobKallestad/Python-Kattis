tick_to_degree = 9
while True:
    pos, first, second, third = map(int, input().split())
    total_turned = 1080  # 3 full turns
    if pos == first == second == third == 0:
        break
    total_turned += tick_to_degree*(pos-first if first <= pos else 40-first+pos)
    total_turned += tick_to_degree*(second-first if first < second else 40-first+second)
    total_turned += tick_to_degree*(second-third if third < second else 40-third+second)
    print(total_turned)
