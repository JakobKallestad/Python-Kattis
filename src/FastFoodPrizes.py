n_test_cases = int(input())

for _ in range(n_test_cases):
    total_won = 0
    n, m = map(int, input().split())
    prizes = []
    for _ in range(n):
        inp = list(map(int, input().split()))
        requirments = inp[1:-1]
        p_value = inp[-1]
        prizes.append((requirments, p_value))
    stickers = list(map(int, input().split()))

    # Then try to decrease untill no more prizes can be won :)
    for (req, value) in prizes:
        while all(stickers[i-1] for i in req):
            for i in req:
                stickers[i-1] -= 1
            total_won += value

    print(total_won)
