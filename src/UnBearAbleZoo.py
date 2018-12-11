from collections import defaultdict

count = 1
while True:
    n = int(input())
    if n == 0:
        break
    animal_dct = defaultdict(int)
    for _ in range(n):
        animal_dct[input().split()[-1].lower()] += 1
    animal_list = sorted(animal_dct.items(), key=lambda x: x[0])
    print("List {}:".format(count))
    for k, v in animal_list:
        print("{} | {}".format(k, v))
    count += 1


