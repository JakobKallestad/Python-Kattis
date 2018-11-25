case = 1
while True:
    try:
        num_list = list(map(int, input().split()[1:]))
        num_max = max(num_list)
        num_min = min(num_list)
        print("Case {}: {} {} {}".format(case, num_min, num_max, num_max-num_min))
        case += 1

    except:
        break