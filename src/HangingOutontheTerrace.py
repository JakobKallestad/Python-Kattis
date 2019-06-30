safety_limit, n_events = map(int, input().split())
current_people = 0
rejected_groups = 0
for _ in range(n_events):
    action, num = input().split()
    num = int(num)
    if action == "enter":
        if current_people + num > safety_limit:
            rejected_groups += 1
        else:
            current_people += num
    else:
        current_people -= num

print(rejected_groups)
