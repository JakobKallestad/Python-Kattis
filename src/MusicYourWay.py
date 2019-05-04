cols = {name: i for i, name in enumerate(input().split())}
n_rows = int(input())
songs = [input().split() for _ in range(n_rows)]
n_sorts = int(input())
for _ in range(n_sorts):
    ind = cols[input()]
    songs = sorted(songs, key=lambda x: x[ind])
    for key in cols.keys():
        print(key, end=' ')
    print()
    for song in songs:
        print(' '.join(song))
    print()