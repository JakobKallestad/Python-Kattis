n_rules, n_iterations = map(int, input().split())
rules = {}
for _ in range(n_rules):
    line = input().split(" -> ")
    rules[line[0]] = line[1]
sequence = list(input())

for _ in range(n_iterations):
    next_sequence = []
    for c in sequence:
        if c in rules:
            next_sequence.append(rules[c])
        else:
            next_sequence.append(c)
    sequence = list(''.join(next_sequence))
print(''.join(sequence))


'''

3 4
A -> AAX
B -> CC
C -> A
B
'''