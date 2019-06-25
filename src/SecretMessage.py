from math import sqrt, ceil

n_test_cases = int(input())
for _ in range(n_test_cases):
    line = list(input())
    m = ceil(sqrt(len(line)))
    while len(line) != m**2:
        line.append("*")
    before = []
    for i in range(0, len(line), m):
        before.append(line[i:i+m])
    after = list(zip(*before))
    result = ''.join([''.join(sub[::-1]) for sub in after]).replace('*', '')
    print(result)
