test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    mydict = d = {chr(k): k for k in range(97, 97+n)}
    deck = [chr(i) for i in range(97, 97+n)]
    for i in range(1, n):
        for sw in range(i):
            temp = deck[0]
            del deck[0]
            deck.append(temp)
        card = deck[0]
        mydict[card] = i
        del deck[0]
    mydict[deck[0]] = n
    for v in mydict.values():
        print(v, end=' ')