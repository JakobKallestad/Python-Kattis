from collections import deque

n_test_cases = int(input())
for _ in range(n_test_cases):
    n, m, l = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    fallen = set()

    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)

    for _ in range(l):
        u = int(input())
        fallen.add(u)
        queue = deque()
        queue.append(u)

        while queue:
            current = queue.popleft()
            for nbr in graph[current]:
                if nbr not in fallen:
                    fallen.add(nbr)
                    queue.append(nbr)

    print(len(fallen))
