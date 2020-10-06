from functools import reduce
nums = [int(c) for c in input()]
while len(nums) > 1:
    n = reduce(lambda x, y: x*y if y > 0 else x, nums)
    nums = [int(c) for c in str(n)]
print(nums[0])