from _operator import add
from functools import reduce

input()
nums = [int(n) for n in input().split()]
nums.sort(reverse=True)
alice = reduce(add, nums[::2])
if len(nums) > 1:
    bob = reduce(add, nums[1::2])
else:
    bob = 0
print(alice, bob)
