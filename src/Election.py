from collections import defaultdict, Counter

n_candidates = int(input())
candidates = {}
for _ in range(n_candidates):
    person = input()
    party = input()
    candidates[person] = party
n_votes = int(input())
votes = defaultdict(int)
for _ in range(n_votes):
    votes[input()] += 1
votes = Counter(votes)
winners = votes.most_common(2)
if winners[0][1] == winners[1][1]:
    print("tie")
else:
    print(candidates[winners[0][0]])