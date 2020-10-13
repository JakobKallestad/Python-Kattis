n, m = map(int, input().split())
moves = [list(input()) for _ in range(n)]
print(1 + list(map(''.join, zip(*moves))).count('_'*n))