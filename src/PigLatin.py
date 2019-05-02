text = []
while True:
    try:
        text.append(input().split())
    except EOFError:
        break

vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
for line in text:
    translated = []
    for word in line:
        if word[0] in vowels:
            translated.append(word+"yay")
        else:
            i = 0
            while word[i] not in vowels:
                i += 1
            translated.append(word[i:] + word[:i] + "ay")
    print(' '.join(translated))


