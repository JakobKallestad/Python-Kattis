p, t = map(int, input().split())
people = {(i+1): set() for i in range(p)}

while True:
    try:
        pers, tree = map(int, input().split())
        people[pers].add(tree)
    except EOFError:
        break

super_set = set()
for opinion in people.values():
    op = tuple(sorted(tuple(opinion)))
    super_set.add(op)
print(len(super_set))
