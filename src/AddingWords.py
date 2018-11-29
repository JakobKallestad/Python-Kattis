memory = {}

def do_stuff():
    line_list = list(input().split())
    if line_list[0] == 'clear':
        memory.clear()
    elif line_list[0] == 'def':
        if line_list[1] in memory:
            del memory[memory[line_list[1]]] # wow, that's one ugly line!
        memory[line_list[1]] = int(line_list[2])
        memory[int(line_list[2])] = line_list[1]
    else:
        line_list.insert(1, '+')
        sum = 0
        all_good = True
        for i in range(2, len(line_list), 2):
            e = line_list[i]
            if e not in memory:
                all_good = False
                break
            if line_list[i-1] == '+':
                sum += memory[line_list[i]]
            elif line_list[i-1] == '-':
                sum -= memory[line_list[i]]
        print(' '.join(line_list[2:]), end=' ')
        if all_good and sum in memory:
            print(memory[sum])
        else:
            print("unknown")


if __name__ == '__main__':
    while True:
        try:
            do_stuff()
        except:
            break

