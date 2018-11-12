case_number = 1
while True:
    try:
        n = int(input())
        print("Case {}:".format(case_number))
        my_numbers = [int(input()) for i in range(n)]
        my_numbers = sorted(my_numbers)
        #print(my_numbers)
        m = int(input())
        for _ in range(m):
            closest_abs = float('inf')
            closest_real = float('inf')
            q = int(input())
            for a in my_numbers:
                low = 0
                high = len(my_numbers)
                while(low < high):
                    mid = (low+high)//2
                    #print('mid',mid)

                    if a != my_numbers[mid]:
                        v = abs(q-(a + my_numbers[mid]))
                        #print('a',a,' ','mid',mid,' ','mid_num',my_numbers[mid],' ','v',v,' ','q',q,' ') # test
                        if v < closest_abs:
                            closest_abs = v
                            closest_real = a + my_numbers[mid]
                    if a+my_numbers[mid] < q:
                        low = mid + 1
                    elif a+my_numbers[mid] > q:
                        high = mid - 1
                    else:
                        high = mid - 1 #this is wrong

            print("Closest sum to {} is {}.".format(q, closest_real))
        case_number += 1
    except EOFError:
        break