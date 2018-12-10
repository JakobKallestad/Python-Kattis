test_cases = int(input())
for _ in range(test_cases):
    input()
    n_children = int(input())
    total_candy = 0
    for child in range(n_children):
        total_candy += int(input())
    print("YES") if total_candy % n_children == 0 else print("NO")
