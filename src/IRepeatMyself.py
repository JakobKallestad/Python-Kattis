n = int(input())
for _ in range(n):
    inp = list(input())
    f_c = inp[0]
    min_rep = 1
    current_repeat = [f_c]
    cr_index = 0
    for i, c in enumerate(inp, 1):
        if c == current_repeat[cr_index]:
            cr_index = (cr_index + 1) % len(current_repeat)
        else:
            cr_index = (1 if c == f_c else 0)
            min_rep = i-cr_index
            current_repeat = inp[:i-cr_index]
    print(min_rep)




