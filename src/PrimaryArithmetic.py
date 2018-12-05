while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    carries = 0
    current_carry = 0
    while a > 0 or b > 0:
        one = a % 10
        two = b % 10
        if one + two + current_carry >= 10:
            carries += 1
            current_carry = 1
        else:
            current_carry = 0
        a //= 10
        b //= 10
    if carries == 0:
        carries = 'No'
    print("{} carry operation{}.".format(carries, '' if carries == 'No' or carries < 2 else 's'))

