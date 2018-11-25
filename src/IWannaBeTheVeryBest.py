n, k = map(int, input().split())
pokemon = list()
team = set()

for _ in range(n):
    pokemon.append(tuple(map(int, input().split())))

pokemon.sort(key=lambda x: x[0], reverse=True)
for i in range(k):
    team.add(pokemon[i])


pokemon.sort(key=lambda x: x[1], reverse=True)
for i in range(k):
    team.add(pokemon[i])


pokemon.sort(key=lambda x: x[2], reverse=True)
for i in range(k):
    team.add(pokemon[i])

print(len(team))
