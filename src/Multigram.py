from collections import Counter

word = list(input())
l_word = len(word)
l_word_half = l_word//2
size = 1
answer = '-1'


def solved():
    global answer, size, l_word, word
    if l_word % size != 0:
        return False
    original_counts = Counter(word[0:size])
    for i in range(size, l_word, size):
        if l_word - i < size:
            return False
        next_counts = Counter(word[i:i+size])
        if original_counts != next_counts:
            return False
    answer = word[0:size]
    return True

while size <= l_word_half and not solved():
    size += 1
print(''.join(answer))