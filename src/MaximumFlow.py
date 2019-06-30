# Edmonds Karp is too slow for this task. I did not check my bigO's beforehand. The way to go is Dinics alg,
# Could also try regular Ford Fulkersons

from collections import deque


def bfs(graph, parent, s, t, n):
    for i in range(n):
        parent[i] = 0
    visited = [False]*n
    queue = deque()
    visited[s] = True
    queue.append(s)
    parent[s] = -1

    while queue:
        u = queue.popleft()
        for v in range(n):
            if not visited[v] and graph[u][v] > 0:
                visited[v] = True
                queue.append(v)
                parent[v] = u
                if v == t:
                    return True
    return False


n, m, s, t = map(int, input().split())
edges_used = set()
edges = set()
parent = [0]*n
max_flow = 0
graph = [[0]*n for _ in range(n)]

for _ in range(m):
    u, v, c = map(int, input().split())
    edges.add((u, v))
    graph[u][v] = c


while bfs(graph, parent, s, t, n):
    flow = float('inf')
    v = t
    while v != s:
        u = parent[v]
        #if (u, v) in edges:
        edges_used.add((u, v))
        flow = min(flow, graph[u][v])
        v = u

    max_flow += flow
    v = t
    while v != s:
        u = parent[v]
        graph[u][v] -= flow
        graph[v][u] += flow
        v = u

print(n, max_flow, len(edges_used))
#edges_used = sorted(edges_used)
for u, v in edges_used:
    print(u, v, graph[v][u])

