input()
stuff = list(map(int, input().split()))
stuff.sort(reverse=True)
count = 1
discount = sum(stuff[2::3])
print(discount)