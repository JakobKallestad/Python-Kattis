
unique = set()

while True:
    try:
        line = input().split()
        fin = []
        for word in line:
            if word.lower() not in unique:
                unique.add(word.lower())
                fin.append(word)
            else:
                fin.append('.')
        print(" ".join(fin))
    except:
        break