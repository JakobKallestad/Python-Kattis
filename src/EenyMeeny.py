ryhme = len(input().split())
n_people = int(input())
people = []
for _ in range(n_people):
    people.append(input())
team_a = []
team_b = []
current = -1
count = 0
while count < n_people:
    current = (current+ryhme)%len(people)
    if count % 2 == 0:
        team_a.append(people[current])
    else:
        team_b.append(people[current])
    people.pop(current)
    current -= 1
    count += 1
print(len(team_a), *team_a, len(team_b), *team_b, sep='\n')
