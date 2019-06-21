a, b, c, d = map(int, input().split())
aa, bb, cc = d // a + 1, d // b + 1, d // c + 1
nums = []
current_num = 0
for i in range(aa):
    current_num = a * i
    if current_num > d:
        break
    for j in range(bb):
        current_num += b * j
        if current_num > d:
            break
        for k in range(cc):
            current_num += c * k
            if current_num > d:
                current_num -= c * k
                break
            if current_num == d:
                nums.append((i, j, k))
            current_num -= c * k
        current_num -= b * j
nums = sorted(nums)
if not nums:
    print("impossible")
else:
    for n in nums:
        print(n[0], n[1], n[2])
