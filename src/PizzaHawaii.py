n_test_cases = int(input())
for _ in range(n_test_cases):
    n_pizza = int(input())
    foreign_pizza = []
    english_pizza = []
    foreign_ingredients = set()
    english_ingredients = set()
    for _ in range(n_pizza):
        p_name = input()
        foreign = set(input().split()[1:])
        english = set(input().split()[1:])
        foreign_pizza.append(foreign)
        english_pizza.append(english)
        foreign_ingredients.update(foreign)
        english_ingredients.update(english)

    foreign_ingredients = sorted(foreign_ingredients)

    for ing in foreign_ingredients:
        all_possible = english_ingredients.copy()
        for i in range(n_pizza):
            if ing in foreign_pizza[i]:
                all_possible.intersection_update(english_pizza[i])
            else:
                all_possible = all_possible - english_pizza[i]
        for ap in sorted(all_possible):
            print(f"({ing}, {ap})")
    print()

