from collections import deque


def get_ceil_index(arr, T, l, r, key):
    while r - l > 1:
        m = l + (r - l) // 2
        if arr[T[m]] >= key:
            r = m
        else:
            l = m
    return r


def LIS(arr, n):
    tail_indices = [0 for _ in range(n + 1)]
    prev_indices = [-1 for _ in range(n + 1)]
    lis_len = 1
    for i in range(1, n):
        if arr[i] < arr[tail_indices[0]]:
            tail_indices[0] = i

        elif arr[i] > arr[tail_indices[lis_len - 1]]:
            prev_indices[i] = tail_indices[lis_len - 1]
            tail_indices[lis_len] = i
            lis_len += 1

        else:
            pos = get_ceil_index(arr, tail_indices, -1, lis_len - 1, arr[i])
            prev_indices[i] = tail_indices[pos - 1]
            tail_indices[pos] = i

    result = deque()
    i = tail_indices[lis_len - 1]
    while i != -1:
        result.appendleft(i)
        i = prev_indices[i]
    print(lis_len)
    if lis_len < len(result):
        print(str(result).replace(',', '')[9:-2])
    else:
        print(str(result).replace(',', '')[7:-2])


while True:
    try:
        n = int(input())
        arr = list(map(int, input().split()))
        LIS(arr, n)
    except EOFError:
        break

'''
14
100 102 5 5 5 5 9 9 9 9 6 6 10 12
'''

'''
10
3 1 2 3 4 5 6 7 8 9
'''

'''
11
3 1 1 2 3 4 5 6 7 8 9
'''