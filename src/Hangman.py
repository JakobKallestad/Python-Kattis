word = set(input())
guesses = input()
lives = 10
ind = 0
while lives:
    if guesses[ind] in word:
        word.remove(guesses[ind])
        if len(word) == 0:
            print("WIN")
            break
    else:
        lives -= 1
    ind += 1
else:
    print("LOSE")
