for _ in range(int(input())):
    phone_nums = [input() for _ in range(int(input()))]
    all_good = True
    for num in phone_nums:
        if any(n.startswith(num) and n != num for n in phone_nums):
            all_good = False
            break
    print("YES") if all_good else print("NO")
