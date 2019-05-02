hard_consonants = {'b', 'c', 'd', 'g', 'k', 'n', 'p', 't'}
endings = {'a', 'o', 'u'}


def find_closest(c, check_list = endings, ending = True):
    replace_c = None
    current_closest = float('inf')
    for e in check_list:
        v = abs(ord(c)-ord(e))
        if v < current_closest:
            replace_c = e
            current_closest = v
        if v == current_closest and ord(e) < ord(replace_c):
            replace_c = e
            current_closest = v
    if ending:
        replace_c += 'h'
    return replace_c


inp = list(input())
sc = inp[0].lower()

replace_c = None
second_syllable = False

translated_fin = []

for i in range(len(inp)):

    # Case -:
    if inp[i] == '-':
        second_syllable = True

    # Case 0 - space sign:
    elif inp[i] == ' ':
        translated_fin += ' '
        replace_c = None
        second_syllable = False

    # Case 1 - start of word:
    elif replace_c is None:
        replace_c = find_closest(inp[i].lower(), hard_consonants, False)
        if inp[i].isupper():
            translated_fin += replace_c.upper()
        else:
            translated_fin += replace_c

        # Case 1.5 - end of word:
        if i == len(inp) - 1 or inp[i + 1] == ' ':
            translated_fin += find_closest(replace_c.lower())

    # Case 3 - hard consonant:
    elif inp[i] in hard_consonants:
        cur_c = inp[i]
        if second_syllable:
            cur_c = replace_c
        translated_fin += cur_c
        if i == len(inp)-1 or inp[i+1] == ' ':
            translated_fin += find_closest(cur_c.lower())

    # Case 4 - nothing special:
    else:
        translated_fin += inp[i]

print(''.join(translated_fin))

