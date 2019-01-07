win_sequence = list(input())
current_level = 25
current_stars = 0
win_streak = 0
legend = False

star_requirment = {21: 2, 16: 3, 11: 4, 1: 5}


def check_rank():
    global current_level, current_stars, legend

    if current_level < 1:
        return  # legend

    max_stars = None
    for key, value in star_requirment.items():
        if current_level >= key:
            max_stars = value
            break
    else:
        if max_stars is None:
            return  # legend

    if current_stars > max_stars:
        current_level -= 1
        current_stars = current_stars-max_stars
    if current_stars < 0:
        if current_level == 20:
            current_stars = 0
        else:
            current_level += 1
            # Need to find the rank again in order to find n_stars
            for key, value in star_requirment.items():
                if current_level >= key:
                    current_stars = value-1
                    break


for game in win_sequence:
    if game == 'W':
        current_stars += 1
        win_streak += 1
        if win_streak >= 3 and current_level >= 6:
            current_stars += 1

    else:
        win_streak = 0
        if 1 <= current_level <= 20:
            current_stars -= 1

    check_rank()

if current_level < 1:
    print("Legend")
else:
    print(current_level)
