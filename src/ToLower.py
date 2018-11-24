import re

p, t = map(int, input().split())
passed = 0
for _ in range(p):
    failed = False
    for _ in range(t):
        line = input()
        if len(line) == 1:
            continue
        if len(re.findall(r'[A-Z]', line[1:])) != 0:
            failed = True
    if not failed:
        passed += 1
print(passed)
