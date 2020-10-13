count = 1
while True:
    try:
        e, m = map(int, input().split())
        i = 0
        while not (e % 365 == 0 and m % 687 == 0):
            e += 1
            m += 1
            i += 1
        print(f"Case {count}: {i}")
        count += 1
    except EOFError:
        break

