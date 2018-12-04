test_cases = int(input())

for _ in range(test_cases):
    input()
    n_godzilla, n_mecha = map(int, input().split())
    godzilla = list(map(int, input().split()))
    mecha = list(map(int, input().split()))
    godzilla.sort()
    mecha.sort()

    while godzilla and mecha:
        if godzilla[0] > mecha[0]:
            del mecha[0]
        elif mecha[0] > godzilla[0]:
            del godzilla[0]
        else:
            del mecha[0]

    print("Godzilla") if godzilla else print("MechaGodzilla")