def solve():
    n_restaurants = int(input())
    for _ in range(n_restaurants):
        n_items = int(input())
        name = input()
        dishes = set()
        for _ in range(n_items):
            dish = input()
            dishes.add(dish)
        if "pea soup" in dishes and "pancakes" in dishes:
            print(name)
            return
    print("Anywhere is fine I guess")


solve()
