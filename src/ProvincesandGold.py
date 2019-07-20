g, s, c = map(int, input().split())
total_money = g*3 + s*2 + c
if total_money >= 8:
    print("Province or ", end='')
elif total_money >= 5:
    print("Duchy or ", end='')
elif total_money >= 2:
    print("Estate or ", end='')

if total_money >= 6:
    print("Gold")
elif total_money >= 3:
    print("Silver")
else:
    print("Copper")
