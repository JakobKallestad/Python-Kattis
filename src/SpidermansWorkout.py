n_test_cases = int(input())
for _ in range(n_test_cases):
    n_intervals = int(input())
    intervals = list(map(int, input().split()))
    dp_table = [[float('inf')]*1001 for _ in range(n_intervals)]
    dp_table[0][intervals[0]] = intervals[0]

    for i in range(n_intervals-1):
        for j in range(1001):
            if dp_table[i][j] != float('inf'):
                dp_table[i+1][j+intervals[i+1]] = max(j + intervals[i+1], dp_table[i][j])
                if j - intervals[i+1] >= 0:
                    dp_table[i+1][j-intervals[i+1]] = min(dp_table[i+1][j-intervals[i+1]], dp_table[i][j])

    if dp_table[n_intervals-1][0] == float('inf'):
        print("IMPOSSIBLE")
    else:
        result = []
        ci = 0
        for i in range(n_intervals-1, 0, -1):
            ci1 = dp_table[i-1][ci+intervals[i]]
            if ci-intervals[i] >= 0:
                ci2 = dp_table[i-1][ci-intervals[i]]
            else:
                ci2 = float('inf')

            if ci1 <= ci2:
                ci += intervals[i]
                result += 'D'
            else:
                ci -= intervals[i]
                result += 'U'

        print('U' + ''.join(result[::-1]))
