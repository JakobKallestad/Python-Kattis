from collections import Counter

word = Counter(input())
word = sorted(word.items(), key=lambda x: x[1])
n_letters = len(word)
n_removed = 0
i = 0
while n_letters > 2:
    n_removed += word[i][1]
    i += 1
    n_letters -= 1
print(n_removed)
