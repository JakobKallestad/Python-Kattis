SIMON = slice(0, 11)
for _ in range(int(input())):
    line = input()
    print(line[11:]) if line[SIMON] == "simon says " else print()
