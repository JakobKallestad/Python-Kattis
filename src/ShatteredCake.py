w = int(input())
n = int(input())
pieces = []

for _ in range(n):
    piece_w, piece_l = map(int, input().split())
    pieces.append(piece_w * piece_l)
print(int(sum(pieces)/w))
