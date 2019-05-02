import itertools


def stuff():
    for i in range(1, 21):
        comb = itertools.combinations(num_list, i)
        for co in comb:
            total = sum(co)
            if total in current_sums:
                print(' '.join(map(str, current_sums[total])))
                print(' '.join(map(str, co)))
                return True
            else:
                current_sums[total] = co
    return False


n_test_cases = int(input())
for i in range(n_test_cases):
    print("Case #{}:".format(i+1))
    num_list = list(map(int, input().split()))
    num_list = sorted(num_list[1:])
    current_sums = {}
    if not stuff():
        print("Impossible")

