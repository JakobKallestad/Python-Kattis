from collections import defaultdict

while True:
    try:
        line = input()
    except EOFError:
        break

    sz = 1
    while sz < len(line):
        all_subs = defaultdict(int)
        for i in range(0, len(line)-sz+1):
            sub_line = line[i:i+sz]
            all_subs[sub_line] += 1
        if min(all_subs.values()) <= 1:
            break
        sz += 1
    print(sz - 1)
