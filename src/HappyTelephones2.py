while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    start_call = []
    end_call = []
    for _ in range(n):
        _, _, start, duration = map(int, input().split())
        start_call.append(start)
        end_call.append(start + duration)

    for _ in range(m):
        start, duration = map(int, input().split())
        end = start + duration
        max_operators = 0
        for i in range(n):
            if start < end_call[i] and end > start_call[i]:
                max_operators += 1
        print(max_operators)
