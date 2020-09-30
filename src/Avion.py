blimps = []
for i in range(1, 6):
    reg_code = input()
    if "FBI" in reg_code:
        blimps.append(i)
print(*blimps) if blimps else print("HE GOT AWAY!")
