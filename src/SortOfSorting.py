while True:
    n_names = int(input())
    if n_names == 0:
        break
    names = []
    for _ in range(n_names):
        names.append(input())
    names = sorted(names, key= lambda x: x[:2])
    for name in names:
        print(name)
    print()