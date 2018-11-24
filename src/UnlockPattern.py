import math

grid = list()
grid.append(list(map(int, input().split())))
grid.append(list(map(int, input().split())))
grid.append(list(map(int, input().split())))
#for line in grid:
    #print(line)

cordinate_dict = {}
for i, y in enumerate(grid):
    for j, x in enumerate(y):
        cordinate_dict[x] = (i,j)

#print(cordinate_dict)

total_distance = 0
for i in range(1, 9):
    current = cordinate_dict[i]
    target = cordinate_dict[i+1]
    dist_to_target = math.sqrt(abs(current[0]-target[0])**2 + abs(current[1]-target[1])**2)
    total_distance += dist_to_target

print(total_distance)