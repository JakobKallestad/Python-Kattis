
def solve():
    words = []
    done = False
    while True:
        try:
            line = input()
            if line == "":
                break
            words.append(line[::-1])
        except EOFError:
            done = True
            break
    words = sorted(words)
    words = [w[::-1] for w in words]
    width = max([len(w) for w in words])
    for w in words:
        print(w.rjust(width))
    if not done:
        print()
    return done


while not solve():
    pass
