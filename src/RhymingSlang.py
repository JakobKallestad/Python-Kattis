common_word = input()
n_ryhmes = int(input())
rhyme_lists = []
for _ in range(n_ryhmes):
    rhyme_lists.append(input().split())
n_test = int(input())
for _ in range(n_test):
    line = input()
    last_word = line.split()[-1]
    for l in rhyme_lists:
        common_OK = False
        new_OK = False
        for word in l:
            if last_word.endswith(word):
                new_OK = True
            if common_word.endswith(word):
                common_OK = True
        if new_OK and common_OK:
            print("YES")
            break
    else:
        print("NO")
