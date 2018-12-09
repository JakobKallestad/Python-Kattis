t_nine = {2: {'a', 'b', 'c'}, 3: {'d', 'e', 'f'}, 4: {'g', 'h', 'i'}, 5: {'j', 'k', 'l'}, 6: {'m', 'n', 'o'},
          7: {'p', 'q', 'r', 's'}, 8: {'t', 'u', 'v'}, 9: {'w', 'x', 'y', 'z'}}
n = int(input())
known_words = []
for _ in range(n):
    known_words.append(input())
keys_pressed = list(map(int, input()))
total_words = 0
for word in known_words:
    if len(word) == len(keys_pressed) and all(word[i] in t_nine[keys_pressed[i]] for i in range(len(word))):
        total_words += 1
print(total_words)