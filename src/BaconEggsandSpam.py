from collections import OrderedDict, defaultdict

while True:
    n = int(input())
    if n == 0:
        break

    people = []
    ingredients = defaultdict(set)
    for _ in range(n):
        line = input().split()
        person = line[0]
        for i in range(1, len(line)):
            ingredients[line[i]].add(person)

    ing = OrderedDict(sorted(ingredients.items()))
    for key, value in ing.items():
        value = sorted(value)
        print(key, ' '.join(value))
