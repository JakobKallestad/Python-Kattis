input()
busses = [int(x) for x in input().split()]
busses.sort()
busses.append(2000)

result_list = []
adding = 0
start = busses[0]
for b in busses[1:]:
    if start == b-adding-1:
        adding += 1

    else:
        if adding == 1:
            result_list.append(str(start))
            result_list.append(str(start+1))
        elif adding > 1:
            add_str = '{}-{}'.format(start, start+adding)
            result_list.append(add_str)
        else:
            result_list.append(str(start))
        start = b
        adding = 0
print(' '.join(result_list))
