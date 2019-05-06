_, A, B = map(list, input().split())
red = 0
blue = 0

for i in range(len(A)):
    if A[i] == B[i]:
        A[i] = B[i] = 'Ø'
        red += 1

A = sorted(A)
B = sorted(B)

i = 0
j = 0
while i < len(A) and j < len(B):
    if A[i] == 'Ø' or B[j] == 'Ø':
        break
    if A[i] == B[j]:
        blue += 1
        i += 1
        j += 1
    elif A[i] < B[j]:
        i += 1
    else:
        j += 1

print(red, blue)
