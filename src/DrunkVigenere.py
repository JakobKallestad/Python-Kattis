line = input()
key = input()
ord_to_chr = {i:chr(65+i) for i in range(26)}
result = []

for i, (l, k) in enumerate(zip(line, key)):
    if i % 2 == 0:
        val = (ord(l) - ord(k))
        if val >= 0:
            result.append(ord_to_chr[val%26])
        else:
            result.append(ord_to_chr[26+val])
    else:
        result.append(ord_to_chr[(ord(l)+ord(k))%26])
print(*result, sep='')