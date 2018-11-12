n = int(input())
for i in range(n):
    line = input()
    line = line.lower()
    bag = set()
    for c in line:
        if 97 <= ord(c) <= 122:
            bag.add(ord(c))
    if len(bag) == 26:
        print("pangram")
    else:
        fin_list = []
        for j in range(97,123):
            if j not in bag:
                fin_list.append(chr(j))
        print("missing", ''.join(fin_list))
