from collections import deque, defaultdict


def bfs(adj, start, goal):
    visited = set()
    parentOf = defaultdict(int)
    queue = deque
    while queue:
        current = queue.pop()
        for nbr in adj[current]:
            if nbr not in visited:
                visited.add(nbr)
                parentOf[nbr] = current
            if nbr == goal:
                return True
    return False

