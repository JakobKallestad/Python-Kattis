price_list = list(map(int, input().split()))
price_list.insert(0,0)
#print(price_list)
truck1 = list(map(int, input().split()))
truck2 = list(map(int, input().split()))
truck3 = list(map(int, input().split()))

total_cost = 0

for i in range(1,100):
    parked = 0
    if truck1[0] <= i < truck1[1]:
        parked += 1
    if truck2[0] <= i < truck2[1]:
        parked += 1
    if truck3[0] <= i < truck3[1]:
        parked += 1
    total_cost += parked*price_list[parked]
    #print(parked*price_list[parked])
print(total_cost)