while True:
    n = int(input())
    if n == -1:
        break

    verticies = []
    for _ in range(n):
        vert = {i for i, v in zip(range(n), list(map(int, input().split()))) if v == 1}
        verticies.append(vert)

    weak = []
    for i in range(n):
        strong = False
        neighbours = verticies[i]
        for j in neighbours:
            neighbours_neighbours = verticies[j]
            for k in neighbours:
                if k in neighbours_neighbours:
                    strong = True
        if not strong:
            weak.append(i)
    print(*weak)



