n = int(input())
nums = list(map(int, input().split()))
result = [nums[0]]
for e in nums[1:]:
    if e > result[-1]:
        result.append(e)
print(len(result))
print(str(result)[1:-1].replace(',', ''))
