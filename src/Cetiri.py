nums = [int(n) for n in input().split()]
nums.sort()
if ((max(nums)-min(nums))%3 != 0):
    print(nums[-1] + (nums[-1]-nums[-2]))
else:
    if nums[1]-nums[0] > nums[2]-nums[1]:
        print((nums[0]+nums[1])//2)
    else:
        print((nums[1]+nums[2])//2)