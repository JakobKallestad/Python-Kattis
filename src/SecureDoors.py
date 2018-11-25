n = int(input())

dict = {}
for _ in range(n):
    action, name = input().split()
    if name not in dict:
        dict[name] = False

    if action == "entry":
        print(name, "entered", end=' ')
        if dict[name]:
            print("(ANOMALY)")
        else:
            print('\n')
        dict[name] = True

    else:
        print(name, "exited", end=' ')
        if not dict[name]:
            print("(ANOMALY)")
        else:
            print('\n')
        dict[name] = False
