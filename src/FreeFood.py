n = int(input())
food =  set()
for _ in range(n):
    start, end = map(int, input().split())
    for i in range(start, end+1):
        food.add(i)
print(len(food))
