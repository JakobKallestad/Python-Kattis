while True:
    max_width = int(input())
    if max_width == 0:
        break
    panels = []
    while True:
        x, y = map(int, input().split())
        if (x, y) == (-1, -1):
            break
        panels.append((x, y))
    current_height, current_width = 0, 0
    row_height, row_width = 0, 0
    for p in panels:
        if p[0] + row_width <= max_width:
            row_width += p[0]
            row_height = max(row_height, p[1])
        else:
            current_height += row_height
            current_width = max(current_width, row_width)
            row_width, row_height = 0, 0
            row_width += p[0]
            row_height = p[1]
    current_height += row_height
    current_width = max(current_width, row_width)
    print(current_width, current_height, sep=' x ')
