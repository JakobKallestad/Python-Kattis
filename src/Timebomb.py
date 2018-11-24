import sys

l1 = input()
l2 = input()
l3 = input()
l4 = input()
l5 = input()

def check_number(n):
    digit = -1
    i = 4*n
    if zero(i):
        digit = 0
    elif one(i):
        digit = 1
    elif two(i):
        digit = 2
    elif three(i):
        digit = 3
    elif four(i):
        digit = 4
    elif five(i):
        digit = 5
    elif six(i):
        digit = 6
    elif seven(i):
        digit = 7
    elif eight(i):
        digit = 8
    elif nine(i):
        digit = 9
    return digit



def zero(n):
    if l1[n:n+3] != "***": return False
    if l2[n:n+3] != "* *": return False
    if l3[n:n+3] != "* *": return False
    if l4[n:n+3] != "* *": return False
    if l5[n:n+3] != "***": return False
    return True


def one(n):
    if l1[n:n+3] != "  *": return False
    if l2[n:n+3] != "  *": return False
    if l3[n:n+3] != "  *": return False
    if l4[n:n+3] != "  *": return False
    if l5[n:n+3] != "  *": return False
    return True


def two(n):
    if l1[n:n+3] != "***": return False
    if l2[n:n+3] != "  *": return False
    if l3[n:n+3] != "***": return False
    if l4[n:n+3] != "*  ": return False
    if l5[n:n+3] != "***": return False
    return True


def three(n):
    if l1[n:n+3] != "***": return False
    if l2[n:n+3] != "  *": return False
    if l3[n:n+3] != "***": return False
    if l4[n:n+3] != "  *": return False
    if l5[n:n+3] != "***": return False
    return True


def four(n):
    if l1[n:n+3] != "* *": return False
    if l2[n:n+3] != "* *": return False
    if l3[n:n+3] != "***": return False
    if l4[n:n+3] != "  *": return False
    if l5[n:n+3] != "  *": return False
    return True


def five(n):
    if l1[n:n+3] != "***": return False
    if l2[n:n+3] != "*  ": return False
    if l3[n:n+3] != "***": return False
    if l4[n:n+3] != "  *": return False
    if l5[n:n+3] != "***": return False
    return True


def six(n):
    if l1[n:n+3] != "***": return False
    if l2[n:n+3] != "*  ": return False
    if l3[n:n+3] != "***": return False
    if l4[n:n+3] != "* *": return False
    if l5[n:n+3] != "***": return False
    return True


def seven(n):
    if l1[n:n+3] != "***": return False
    if l2[n:n+3] != "  *": return False
    if l3[n:n+3] != "  *": return False
    if l4[n:n+3] != "  *": return False
    if l5[n:n+3] != "  *": return False
    return True


def eight(n):
    if l1[n:n+3] != "***": return False
    if l2[n:n+3] != "* *": return False
    if l3[n:n+3] != "***": return False
    if l4[n:n+3] != "* *": return False
    if l5[n:n+3] != "***": return False
    return True


def nine(n):
    if l1[n:n+3] != "***": return False
    if l2[n:n+3] != "* *": return False
    if l3[n:n+3] != "***": return False
    if l4[n:n+3] != "  *": return False
    if l5[n:n+3] != "***": return False
    return True


# 3, 7, 11, 15, 19, 23, 27, 31
l_dict = {3: 1, 7: 2, 11: 3, 15: 4, 19: 5, 23: 6, 27: 7, 31: 8}
n_digits = l_dict[len(l1)]
total_sum = 0

for i in range(n_digits):
    total_sum *= 10
    n = check_number(i)
    if n >= 0:
        total_sum += n
    else:
        total_sum = 1
        break

if total_sum % 6 == 0:
    print("BEER!!")
else:
    print("BOOM!!")
