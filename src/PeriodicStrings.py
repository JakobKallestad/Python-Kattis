
word = list(input())
l_word = len(word)
l_word_half = l_word//2
size = 1


def shift_pattern(pattern):
    return list(pattern[-1]) + pattern[:-1]


def solved():
    global size, l_word, word
    if l_word % size != 0:
        return False
    match_pattern = word[0:size]
    match_pattern = shift_pattern(match_pattern)
    for i in range(size, l_word, size):
        if l_word - i < size:
            return False
        next_pattern = word[i:i+size]
        if match_pattern != next_pattern:
            return False
        match_pattern = shift_pattern(next_pattern)
    return True


while size <= l_word and not solved():
    size += 1
print(size)
