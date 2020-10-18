n = int(input())
word = input()
for i in range(n, 1, -1):
    print(f"{i} bottles of {word} on the wall, {i} bottles of {word}.\nTake one down, pass it around, {i-1} bottle{'s' if i>2 else ''} of {word} on the wall.\n")
print(f"1 bottle of {word} on the wall, 1 bottle of {word}.\nTake it down, pass it around, no more bottles of {word}.")