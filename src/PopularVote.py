test_cases = int(input())
for _ in range(test_cases):
    n = int(input())
    candidates = []
    for _ in range(n):
        candidates.append(int(input()))
    winner = max(candidates)
    winner_index = candidates.index(winner)+1
    no_winner = (candidates.count(winner) > 1)
    majority_winner = winner > sum(candidates)-winner
    if no_winner:
        print("no winner")
    elif majority_winner:
        print("majority winner", winner_index)
    else:
        print("minority winner", winner_index)

