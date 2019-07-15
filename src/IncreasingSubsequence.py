while True:
    nums = list(map(int, input().split()))
    if len(nums) == 1:
        break
    n_nums = nums[0]
    nums = nums[1:]
    liss = [1] * n_nums
    lexio = [[c] for c in nums]
    i = 0
    j = 1
    while j < n_nums:
        while i < j:
            if nums[i] < nums[j]:
                if liss[i] + 1 == liss[j] and lexio[j] > lexio[i] + [nums[j]] or liss[i] + 1 > liss[j]:
                    liss[j] = liss[i] + 1
                    lexio[j] = lexio[i] + [nums[j]]
            i += 1
        j += 1
        i = 0

    longest_liss = -1
    least_lexio = [float('inf')]
    for i in range(n_nums):
        if liss[i] == longest_liss and lexio[i] < least_lexio or liss[i] > longest_liss:
            longest_liss = liss[i]
            least_lexio = lexio[i]
    print(longest_liss, str(least_lexio).replace(',', '')[1:-1])

'''
9 5 10 2 9 17 24 6 14 50
'''
