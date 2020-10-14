chars = ['N', 'S', 'W', 'E']
line = input()


def count_substrings(line, prev_substring, min_length):
    for c in chars:
        sub_string = prev_substring+c
        count = line.count(sub_string)
        if count >= 2:
            saved_chars = (count - 1) * len(sub_string) - count
            min_length = min(min_length, len(line) - saved_chars)
            min_length = min(min_length, count_substrings(line, sub_string, min_length))
    return min_length

min_length = count_substrings(line, '', len(line))
print(min_length)
