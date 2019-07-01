slang = {
    "at": "@",
    "and": "&",
    "one": "1",
    "won": "1",
    "to": "2",
    "too": "2",
    "two": "2",
    "for": "4",
    "four": "4",
    "bea": "bÆ",
    "be": "bÆ",
    "bee": "bÆ",
    "sea": "cÆ",
    "see": "cÆ",
    "eye": "iÆ",
    "oh": "oÆ",
    "owe": "oÆ",
    "are": "rÆ",
    "you": "uÆ",
    "why": "yÆ",

    "At": "@",
    "And": "&",
    "One": "1",
    "Won": "1",
    "To": "2",
    "Too": "2",
    "Two": "2",
    "For": "4",
    "Four": "4",
    "Bea": "BÆ",
    "Be": "BÆ",
    "Bee": "BÆ",
    "Sea": "CÆ",
    "See": "CÆ",
    "Eye": "IÆ",
    "Oh": "OÆ",
    "Owe": "OÆ",
    "Are": "RÆ",
    "You": "UÆ",
    "Why": "YÆ"
}

n_test_cases = int(input())
for _ in range(n_test_cases):
    line = list(input().split())
    result = []
    for w in line:
        indexes = []
        for k, v in slang.items():
            indexes.append((w.find(k), k))
        indexes = sorted(indexes, key=lambda x: -len(x[1]))
        indexes = sorted(indexes, key=lambda x: x[0])
        for pos, word in indexes:
            if pos == -1:
                continue
            w = w.replace(word, slang[word])  # still won't work yet
        w = w.replace('Æ', '')
        result.append(w)
    print(' '.join(result))
