num1 = [int(n) for n in input()]
num2 = [int(n) for n in input()]
while len(num1) < len(num2):
    num1.insert(0, 0)
while len(num2) < len(num1):
    num2.insert(0, 0)

fin_a = []
fin_b = []

for a, b in zip(num1, num2):
    if a == b:
        fin_a.append(a)
        fin_b.append(b)
    elif a < b:
        fin_b.append(b)
    else:
        fin_a.append(a)

while len(fin_a) > 1 and fin_a[0] == 0:
    del fin_a[0]
while len(fin_b) > 1 and fin_b[0] == 0:
    del fin_b[0]

if not fin_a:
    print("YODA")
else:
    print(''.join(map(str, fin_a)))

if not fin_b:
    print("YODA")
else:
    print(''.join(map(str, fin_b)))