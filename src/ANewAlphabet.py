chars = [chr(i) for i in range(97, 123)]
new_chars = ['@', '8', '(', '|)', '3', '#', '6', '[-]', '|', '_|', '|<', '1', '[]\\/[]', '[]\\[]', '0', '|D', '(,)', '|Z',
             '$', "']['", '|_|', '\\/', '\\/\\/', '}{', '`/', '2']
alphabet = dict(zip(chars, new_chars))
translated_line = []
for c in input().lower():
    if c in alphabet:
        translated_line.append(alphabet[c])
    else:
        translated_line.append(c)
print(''.join(translated_line))
