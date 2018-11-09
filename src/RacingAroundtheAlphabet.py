import math

n = int(input())
alpha_list = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," ","'"]
a_len = 28
dist_per_slice = ((60 * math.pi) / 28)

for i in range(n):
    line = input()
    current_index = alpha_list.index(line[0])
    time = 0
    for c in line:
        target_index = alpha_list.index(c)
        distance = abs(current_index-target_index)
        if distance <= 14:
            time += (dist_per_slice * distance)/15
        else:
            time += (dist_per_slice * (a_len - distance))/15
        current_index = target_index
    time += len(line)
    print(time)