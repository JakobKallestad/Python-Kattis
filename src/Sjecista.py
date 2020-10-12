n = int(input())
A = sum([i*(n-2-i) for i in range(1, n-2)])
B = (A*n)//4
print(B)
