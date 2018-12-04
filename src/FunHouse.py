count = 1


def change_dir(y, x, current_index, direction, house):
    change_dict = {('/', "DOWN"): "LEFT", ('/', "UP"): "RIGHT", ('/', "RIGHT"): "UP", ('/', "LEFT"): "DOWN",
                   ('\\', "DOWN"): "RIGHT", ('\\', "UP"): "LEFT", ('\\', "RIGHT"): "DOWN", ('\\', "LEFT"): "UP"}
    new_direction = change_dict[(house[y][x], direction)]
    return new_direction


while True:
    width, height = map(int, input().split())
    if width == height == 0:
        break
    print("HOUSE", count)
    count += 1
    house = []
    current_index = (0, 0)
    direction = None
    for i in range(height):
        row = []
        for j, c in enumerate(input()):
            if c == '*':
                current_index = (i, j)
                row.append('*')
            elif c == '\\':
                row.append("\\")
            else:
                row.append(c)
        house.append(row)

    #for line in house:
    #    print(''.join(line))

    if current_index[0] == 0:
        direction = "DOWN"
    elif current_index[0] == height - 1:
        direction = "UP"
    elif current_index[1] == 0:
        direction = "RIGHT"
    else:
        direction = "LEFT"

    while True:
        y, x = current_index

        if direction == "DOWN":
            current_index = (y + 1, x)
        elif direction == "UP":
            current_index = (y - 1, x)
        elif direction == "RIGHT":
            current_index = (y, x + 1)
        else:
            current_index = (y, x - 1)

        # check new placement:
        y, x = current_index

        if house[y][x] == 'x':
            house[y][x] = '&'
            for line in house:
                print(''.join(line))
            break
        elif house[y][x] == '.':
            pass
        else:
            direction = change_dir(y, x, current_index, direction, house)
