word_list = []
while True:
    try:
        word_list += input().split()
    except:
        break

comb_list = set()
for w1 in word_list:
    for w2 in word_list:
        if w1 != w2:
            new_word = w1+w2
            comb_list.add(new_word)

comb_list = sorted(comb_list)
[print(e) for e in comb_list]