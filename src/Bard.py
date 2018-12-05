n_villagers = int(input())
n_evenings = int(input())

villagers = [set() for _ in range(n_villagers)]
current_song = 0


for _ in range(n_evenings):
    present = list(map(int, input().split()[1:]))
    if 1 in present:
        for v in present:
            villagers[v-1].add(current_song)
        current_song += 1
    else:
        shared_song_knowledge = set()
        for v in present:
            shared_song_knowledge |= villagers[v-1]
        for v in present:
            villagers[v-1] = shared_song_knowledge.copy()

print(1)
for i, v in enumerate(villagers[1:]):
    if v == villagers[0]:
        print(i+2)
