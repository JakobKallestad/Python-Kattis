n = int(input())
fbi_coding = list("0123456789ACDEFHJKLMNPRTVWX")
vals = list(range(28))
fbi_dct = dict(zip(fbi_coding, vals))
ambiguos_letters = {'B': 8, 'G': 11, 'I': 1, 'O': 0, 'S': 5, 'U': 24, 'Z': 2}
fbi_dct.update(ambiguos_letters)
mul_seq = [2, 4, 5, 7, 8, 10, 11, 13]


def mm(c):
    return str(fbi_dct[c])


for test_case_nr in range(1, n + 1):
    ucn = list(input().split()[1])
    value = 0
    for i, c in enumerate(ucn[:-1]):
        value += mul_seq[i] * fbi_dct[c]
    if value % 27 == fbi_dct[ucn[-1]]:
        gg = sum(fbi_dct[ucn[7 - j]] * (27 ** j) for j in range(8))
        print(test_case_nr, gg)
    else:
        print(test_case_nr, "Invalid")
