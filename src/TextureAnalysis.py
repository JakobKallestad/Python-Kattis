n_test_case = 1


def find_pattern(n_test_case):
    inp = input()
    if inp == "END":
        return
    count = 1
    while count < len(inp) and inp[count] != '*':
        count += 1
    for i, c in enumerate(inp):
        if i % count == 0:
            if c == '.':
                print(n_test_case, "NOT EVEN")
                return
        else:
            if c == '*':
                print(n_test_case, "NOT EVEN")
                return
    else:
        print(n_test_case, "EVEN")


while True:
    try:
        find_pattern(n_test_case)
        n_test_case += 1
    except EOFError:
        break
