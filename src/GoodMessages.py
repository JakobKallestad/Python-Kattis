from collections import Counter

offset = int(input())
message = list(input())
n_steps = int(input())
n_unhappy = 0
vowels = {'a', 'e', 'i', 'o', 'u', 'y'}

for _ in range(n_steps):
    vowel_count = 0
    for i in range(len(message)):
        message[i] = chr(97 + (ord(message[i]) - 97 + offset) % 26)
    details = Counter(message)
    for w in vowels:
        if w in details:
            vowel_count += details[w]
    if vowel_count*2 >= len(message)-vowel_count:
        n_unhappy += 1
print("Boris") if n_unhappy < n_steps-n_unhappy else print("Colleague")



'''
1
thequickbrownfoxjumpedoverthelazydog
10
'''

'''
4
banana
3
'''