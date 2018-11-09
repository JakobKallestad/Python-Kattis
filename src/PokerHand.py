from collections import Counter

str_list = input().split()
points = 0

value_list = []
card_values = {"A":1,"T":10,"J":11,"Q":12,"K":13}
for card in str_list:
    if card[0] in card_values:
        value_list.append(card_values[card[0]])
    else:
        value_list.append(int(card[0]))

c = Counter(value_list)
num_most_common = c.most_common(1)[0][1]
print(num_most_common)

