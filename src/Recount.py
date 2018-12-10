from collections import defaultdict

people = defaultdict(int)
while True:
    name = input()
    if name == "***":
        break
    people[name] += 1
people = sorted(people.items(), key=lambda x: x[1], reverse=True)
if people[0][1] == people[1][1]:
    print("Runoff!")
else:
    print(people[0][0])