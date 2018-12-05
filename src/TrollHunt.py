import math
b, k, g = map(int, input().split())
check_per_day = k//g
print(math.ceil((b-1)/check_per_day))
