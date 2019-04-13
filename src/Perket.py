import itertools

n_ingredients = int(input())
ingredients = []
for _ in range(n_ingredients):
    sourness, bitterness = map(int, input().split())
    ingredients.append((sourness, bitterness))

best_perket = float('inf')

for i in range(1, n_ingredients+1):
    subsets = [a for a in itertools.combinations(ingredients, i)]
    for sub in subsets:
        sour_score = 1
        bitter_score = 0
        for ing in sub:
            sour_score *= ing[0]
            bitter_score += ing[1]
        perket = abs(sour_score-bitter_score)
        best_perket = min(best_perket, perket)
print(best_perket)
