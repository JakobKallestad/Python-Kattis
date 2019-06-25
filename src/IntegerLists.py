n_test_cases = int(input())
for _ in range(n_test_cases):
    commands = list(input())
    n_nums = int(input())
    if n_nums == 0:
        input()
        nums = []
    else:
        nums = list(map(int, (input()[1:-1]).split(',')))
    rev = False
    start, end = 0, len(nums)
    for c in commands:
        if c == 'R':
            rev = not rev
        else:
            if rev:
                if end <= start:
                    print("error")
                    break
                end -= 1
            else:
                if start >= end:
                    print("error")
                    break
                start += 1
    else:
        nums = nums[start:end]
        if rev:
            nums = nums[::-1]
        print(str(nums).replace(' ', ''))
