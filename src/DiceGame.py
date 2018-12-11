g_dices = list(map(int, input().split()))
gunnar = (g_dices[0] + g_dices[1]) / 2 + (g_dices[2] + g_dices[3]) / 2
e_dices = list(map(int, input().split()))
emma = (e_dices[0] + e_dices[1]) / 2 + (e_dices[2] + e_dices[3]) / 2
if gunnar > emma:
    print("Gunnar")
elif emma > gunnar:
    print("Emma")
else:
    print("Tie")
