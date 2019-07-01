from collections import deque


class Edge:
    def __init__(self, u, v, cap, equation):
        self.u = u
        self.v = v
        self.cap = cap
        self.flow = 0
        self.residual = None
        self.equation = equation

    def is_residual(self):
        return self.cap == 0

    def remaining_capacity(self):
        return self.cap - self.flow

    def augment(self, bottleneck):
        self.flow += bottleneck
        self.residual.flow -= bottleneck

    def __repr__(self):
        return str(self.u) + " " + str(self.v) + " " + str(self.flow)


def add_edge(u, v, equation, mid_edge):
    e1 = Edge(u, v, 1, equation)
    if mid_edge:
        edges.append(e1)
    e2 = Edge(v, u, 0, "-")
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
                return bottleneck
        next[current] += 1
    return 0


operators = ['+', '-', '*']
n_equations = int(input())
graph = [[] for _ in range(n_equations+20002)]  # try something
answers = {}
count = n_equations+2
s = 0
t = n_equations+1
edges = list()
max_flow = 0


# Source to equations:
for i in range(1, n_equations+1):
    add_edge(s, i, "-", False)


# Equations to answers:
for i in range(1, n_equations+1):
    a, b = input().split()
    for op in operators:
        expr = a + op + b
        ans = eval(expr)
        equation = "{} {} {} = {}".format(a, op, b, ans)
        if ans in answers:
            add_edge(i, answers[ans], equation, True)
        else:
            answers[ans] = count
            add_edge(i, count, equation, True)
            count += 1

# Answers to target:
for co in answers.values():
    add_edge(co, t, "-", False)


# Dinics:
n = n_equations+len(answers) + 4
level = [-1]*n
next = [0]*n
while bfs(level):
    next = [0]*n
    f = dfs(s, next, float('inf'))
    while f:
        max_flow += f
        f = dfs(s, next, float('inf'))

n_good_edges = 0
for e in edges:
    if e.flow == 1:
        n_good_edges += 1

if n_good_edges < n_equations:
    print("impossible")
else:
    for e in edges:
        if e.flow == 1:
            print(e.equation)
