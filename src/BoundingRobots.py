pos_or_neg = {"u":1, "r":1, "d":-1, "l":-1}
while True:
    w, l = map(int, input().split())
    if w == l == 0:
        break
    n = int(input())
    x_actual, y_actual = 0, 0
    x_think, y_think = 0, 0
    for _ in range(n):
        direction, length = input().split()
        length = int(length)
        if direction == "u" or direction == "d":
            y_actual = min(max(0, y_actual+length*pos_or_neg[direction]), l-1)
            y_think += length*pos_or_neg[direction]
        else:
            x_actual = min(max(0, x_actual+length*pos_or_neg[direction]), w-1)
            x_think += length*pos_or_neg[direction]
    print("Robot thinks", x_think, y_think)
    print("Actually at", x_actual, y_actual)
    print()

