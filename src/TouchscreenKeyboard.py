tc = int(input())
qwerty = []
qwerty.append([c for c in "qwertyuiop"])
qwerty.append([c for c in "asdfghjkl"])
qwerty.append([c for c in "zxcvbnm"])
qwerty_dist = {}


def calc_dist(start_y, start_x, start_c):
    for y in range(len(qwerty)):
        for x in range(len(qwerty[y])):
            c = qwerty[y][x]
            qwerty_dist[start_c+c] = abs(start_x-x)+abs(start_y-y)


for y in range(len(qwerty)):
    for x in range(len(qwerty[y])):
        calc_dist(y, x, qwerty[y][x])


for _ in range(tc):
    result = []
    line = input().split()
    target = line[0]
    q = int(line[1])
    for _ in range(q):
        query = input()
        sum = 0
        for c_s, c_t in zip(query, target):
            sum += qwerty_dist[c_s+c_t]
        result.append((sum, query))
    result.sort()
    for r in result:
        print(r[1], r[0])
