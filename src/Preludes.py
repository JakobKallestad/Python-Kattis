note_dict = {'A#': 'Bb', 'C#': 'Db', 'D#': 'Eb', 'F#': 'Gb', 'G#': 'Ab'}
revd = dict([reversed(i) for i in note_dict.items()])
note_dict.update(revd)

for i in range(1,6):
    try:
        note, tonality = input().split()
        print("Case {}:".format(i), end=' ')
        if note in note_dict:
            print(note_dict[note], tonality)
        else:
            print("UNIQUE")

    except:
        break
