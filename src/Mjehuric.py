logs = list(map(int, input().split()))


def swap(i, j):
    logs[i], logs[j] = logs[j], logs[i]


while logs != [1,2,3,4,5]:
    for i in range(len(logs)-1):
        if logs[i] > logs[i+1]:
            swap(i, i+1)
            print(' '.join(map(str, logs)))
