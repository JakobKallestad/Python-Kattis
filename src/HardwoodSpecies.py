from collections import defaultdict

n_trees = 0
trees = defaultdict(int)
while True:
    try:
        trees[input()] += 1
        n_trees += 1
    except EOFError:
        break

trees = sorted(trees.items(), key=lambda x: x[0])

for k, v in trees:
    print(k, (v/n_trees)*100)

# This is too slow in python, but a direct translation to java will pass the test cases
