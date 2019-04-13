def check_score(d1, d2):
    # Check Mia
    if d1 == 1 and d2 == 2 or d1 == 2 and d2 == 1:
        return 1000

    # Check Double:
    if d1 == d2:
        return d1 * 100

    # Normal value
    high = max(d1, d2)
    low = min(d1, d2)
    return int(str(high)+str(low))


while True:
    d1, d2, d3, d4 = map(int, input().split())
    if d1 == d2 == d3 == d4 == 0:
        break

    score_p1 = check_score(d1, d2)
    score_p2 = check_score(d3, d4)

    if score_p1 > score_p2:
        print("Player 1 wins.")
    elif score_p1 < score_p2:
        print("Player 2 wins.")
    else:
        print("Tie.")