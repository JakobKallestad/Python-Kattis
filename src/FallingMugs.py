d = int(input())
dist_dict = {}
for i in range(d+1):
    dist_dict[i**2] = i

for dist, ind in dist_dict.items():
    if (dist+d) in dist_dict:
        print(ind, dist_dict[dist+d])
        break
else:
    print("impossible")
