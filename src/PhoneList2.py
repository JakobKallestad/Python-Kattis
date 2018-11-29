for _ in range(int(input())):
    nums = set()
    illegal_nums = set()
    for _ in range(int(input())):
        line = input()
        for i in range(1, len(line)):
            illegal_nums.add(line[:i])
        nums.add(line)
    print("YES") if len(nums & illegal_nums) == 0 else print("NO")