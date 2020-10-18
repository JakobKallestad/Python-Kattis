specials = {i for i in range(ord('!'), ord('*')+1)}
specials.update({i for i in range(ord('['), ord(']')+1)})

while True:
    try:
        n = int(input())
        current = list(input())
        for _ in range(n):
            next = []
            for c in current:
                if ord(c) in specials:
                    next.append('\\')
                next.append(c)
            current = next
        print(*current, sep='')
    except EOFError:
        break
