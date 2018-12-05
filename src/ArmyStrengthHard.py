test_cases = int(input())

for _ in range(test_cases):
    input()
    n_godzilla, n_mecha = map(int, input().split())
    godzilla = list(map(int, input().split()))
    mecha = list(map(int, input().split()))
    godzilla.sort()
    mecha.sort()
    g = 0
    m = 0

    while g < n_godzilla and m < n_mecha:
        if godzilla[g] > mecha[m]:
            m += 1
        elif mecha[m] > godzilla[g]:
            g += 1
        else:
            m += 1
    print("Godzilla") if g < n_godzilla else print("MechaGodzilla")