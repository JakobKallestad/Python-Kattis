from collections import deque
import sys


class Node:
    def __init__(self, num):
        self.num = num
        self.edges = []
        self.left = False
        self.left_edges = set()


c, p, x, l = map(int, input().split())
x -= 1
l -= 1

if x == l:
    print('leave')
    sys.exit()

countries = [Node(i) for i in range(c)]
for _ in range(p):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    countries[a].edges.append(countries[b])
    countries[b].edges.append(countries[a])


queue = deque()
for e in countries[l].edges:
    e.left_edges.add(l)
    queue.append(e)

while queue:
    current = queue.popleft()
    if current.left:
        continue
    if len(current.left_edges)*2 >= len(current.edges):
        # current will be leaving:
        current.left = True
        if current.num == x:
            print("leave")
            sys.exit()
        for e in current.edges:
            if e.left:
                continue
            e.left_edges.add(current.num)
            queue.append(e)
print("stay")