from collections import deque

want = {'b': '$', 't': '|', 'j': '*'}
n_test_cases = int(input())
for _ in range(n_test_cases):
    path = input().replace('.', '')
    inventory = deque()
    for c in path:
        if c == '$' or c == '*' or c == '|':
            inventory.append(c)
        else:
            try:
                inv = inventory.pop()
            except:
                print("NO")
                break
            if want[c] != inv:
                print("NO")
                break
    else:
        print("YES") if not inventory else print("NO")
