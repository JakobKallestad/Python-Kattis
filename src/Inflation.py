n = int(input())
nums = list(map(int, input().split()))
nums = sorted(nums)
lowest = float('inf')
for i, num in enumerate(nums, start=1):
    if num/i > 1:
        print("impossible")
        break
    if num/i < lowest:
        lowest = num/i
else:
    print(lowest)
