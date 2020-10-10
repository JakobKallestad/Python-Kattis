n = int(input())
nums = {int(input()) for _ in range(n)}
for i in range(1, max(nums)):
    if i not in nums:
        print(i)
if nums == set(range(1, max(nums)+1)):
    print("good job")
