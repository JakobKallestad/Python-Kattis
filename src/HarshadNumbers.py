n = int(input())
while True:
    temp = n
    sum_temp = 0
    while temp > 0:
        sum_temp += temp%10
        temp //= 10
    #print(sum_temp)
    if sum_temp == 0 or n%sum_temp == 0:
        print(n)
        break
    n += 1