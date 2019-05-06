from collections import deque
n_socks = int(input())
socks = deque(list(map(int, input().split()))[::-1])
pile = deque()
n_moves = 0

while socks:
    if pile and socks[-1] == pile[-1]:
        socks.pop()
        pile.pop()
    else:
        pile.append(socks.pop())
    n_moves += 1

print(n_moves) if not pile else print("impossible")