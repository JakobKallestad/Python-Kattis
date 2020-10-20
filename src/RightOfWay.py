dir_to_num = {
    "North": 0,
    "East": 1,
    "South": 2,
    "West": 3
}

a, b, c = map(lambda x: dir_to_num[x], input().split())
if abs(a-b) == 2 and c == (3 if a == 0 else a-1):  #straight
    print("Yes")
elif b == (a+1)%4 and (abs(a-c) == 2 or c == (3 if a == 0 else a-1)):
    print("Yes")
else:
    print("No")

