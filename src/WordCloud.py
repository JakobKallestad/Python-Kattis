from math import ceil

cloud_count = 1
while True:
    max_width, n_words = map(int, input().split())
    if max_width == n_words == 0:
        break

    word_count = {}
    for _ in range(n_words):
        word, count = input().split()
        word_count[word] = int(count)

    max_freq = max(word_count.values())
    total_height = 0
    current_height = 0
    current_width = 0
    for w, c in word_count.items():
        p = 8 + ceil((40*(c-4))/(max_freq-4))
        width = ceil((9/16)*len(w)*p)
        if current_width + width <= max_width:
            current_width += (width + 10)
            current_height = max(current_height, p)
        else:
            total_height += current_height
            current_width = (width + 10)
            current_height = p
    total_height += current_height
    print(f"CLOUD {cloud_count}: {total_height}")
    cloud_count += 1
