from collections import defaultdict

n_people, required_score, n_querries = map(int, input().split())
scores = defaultdict(int)
has_won = set()
for _ in range(n_people):
    input()

for _ in range(n_querries):
    person, points = map(str, input().split())
    points = int(points)
    scores[person] += points
    if scores[person] >= required_score and person not in has_won:
        print(person, " wins!")
        has_won.add(person)
if not has_won:
    print("No winner!")
