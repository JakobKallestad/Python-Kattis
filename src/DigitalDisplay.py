full = ["+---+"]
left = ["|    "]
right = ["    |"]
hollow = ["|   |"]
dots = ["+   +"]
dl = ["    +"]

digits_map = {
    '0': [full, hollow, hollow, dots, hollow, hollow, full],
    '1': [dl, right, right, dl, right, right, dl],
    '2': [full, right, right, full, left, left, full],
    '3': [full, right, right, full, right, right, full],
    '4': [dots, hollow, hollow, full, right, right, dl],
    '5': [full, left, left, full, right, right, full],
    '6': [full, left, left, full, hollow, hollow, full],
    '7': [full, right, right, dl, right, right, dl],
    '8': [full, hollow, hollow, full, hollow, hollow, full],
    '9': [full, hollow, hollow, full, right, right, full],
    ':': [[" "], [" "], ["o"], [" "], ["o"], [" "], [" "]]
}

while True:
    time = input()
    if time == "end":
        print("end")
        break
    answer = [[] for _ in range(7)]
    digits = list(time)

    for j, d in enumerate(digits):
        dig = digits_map[d]
        for i, row in enumerate(dig):
            answer[i][j:j + 5] = row

    for i in range(7):
        print('  '.join(answer[i]))
    print()
    print()
