n_keys, n_queries = map(int, input().split())
dct = {}

for _ in range(n_keys):
    desc, salary = input().split()
    dct[desc] = int(salary)

for _ in range(n_queries):
    salary_sum = 0
    while True:
        line = input()
        if line == '.':
            break
        for word in line.split():
            if word in dct:
                salary_sum += dct[word]
    print(salary_sum)
