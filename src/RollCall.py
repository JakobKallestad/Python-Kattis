names = set()
first_name = set()
call_by_last_name = set()
while True:
    try:
        name = input().split()
        if name[0] in first_name:
            call_by_last_name.add(name[0])
        first_name.add(name[0])
        names.add((name[1], name[0]))
    except EOFError:
        break

names = sorted(names)

for n in names:
    if n[1] in call_by_last_name:
        print(n[1], n[0])
    else:
        print(n[1])
