def check(search, look):
    count = 0
    for i in range(len(look)):
        if look[i:].startswith(search):
            count += 1
    return count


while True:
    line = input()
    if line == '0':
        break
    search, look = line.split()

    type_one = 0
    type_two = 0
    type_three = 0

    type_one = check(search, look)

    mod_set = set()
    for i in range(len(search)):
        search_dummy = list(search)
        search_dummy.pop(i)
        mod_search = ''.join(search_dummy)
        if mod_search not in mod_set:
            type_two += check(mod_search, look)
            mod_set.add(mod_search)

    mod_set = set()
    for i in range(len(search)+1):
        for c in ('A', 'G', 'C', 'T'):
            search_dummy = list(search)
            search_dummy.insert(i, c)
            mod_search = ''.join(search_dummy)
            if mod_search not in mod_set:
                type_three += check(mod_search, look)
                mod_set.add(mod_search)

    print(type_one, type_two, type_three)


