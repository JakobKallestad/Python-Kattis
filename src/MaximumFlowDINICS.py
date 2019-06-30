from collections import deque


class Edge:
    def __init__(self, u, v, cap):
        self.u = u
        self.v = v
        self.cap = cap
        self.flow = 0
        self.residual = None

    def is_residual(self):
        return self.cap == 0

    def remaining_capacity(self):
        return self.cap - self.flow

    def augment(self, bottleneck):
        self.flow += bottleneck
        self.residual.flow -= bottleneck

    def __repr__(self):
        return str(self.u) + " " + str(self.v) + " " + str(self.flow)


def add_edge(u, v, cap):
    e1 = Edge(u, v, cap)
    e2 = Edge(v, u, 0)
    e1.residual = e2
    e2.residual = e1
    graph[u].append(e1)
    graph[v].append(e2)


def bfs(level):
    for i in range(n):
        level[i] = -1
    queue = deque()
    queue.append(s)
    level[s] = 0

    while queue:
        current = queue.popleft()
        for e in graph[current]:
            cap = e.remaining_capacity()
            if cap > 0 and level[e.v] == -1:
                level[e.v] = level[current] + 1
                queue.append(e.v)
    return level[t] != -1


def dfs(current, next, flow):
    if current == t:
        return flow
    numEdges = len(graph[current])
    while next[current] < numEdges:
        e = graph[current][next[current]]
        cap = e.remaining_capacity()
        if cap > 0 and level[e.v] == level[current] + 1:
            bottleneck = dfs(e.v, next, min(flow, cap))
            if bottleneck > 0:
                e.augment(bottleneck)
                edges_used.add(e)
                return bottleneck
        next[current] += 1
    return 0


n, m, s, t = map(int, input().split())
edges_used = set()
graph = [[] for _ in range(n)]
max_flow = 0

for _ in range(m):
    u, v, c = map(int, input().split())
    add_edge(u, v, c)


level = [-1]*n
next = [0]*n
while(bfs(level)):
    next = [0]*n
    f = dfs(s, next, float('inf'))
    while(f):
        max_flow += f
        f = dfs(s, next, float('inf'))

n_good_edges = 0
for e in edges_used:
    if e.cap >= e.flow > 0 and not e.is_residual():
        n_good_edges += 1

print(n, max_flow, n_good_edges)
for e in edges_used:
    if e.cap >= e.flow > 0 and not e.is_residual():
        print(e)


