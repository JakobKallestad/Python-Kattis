current_player = int(input()) - 1
n_questions = int(input())
remaining_time = 210
loser = -1
for _ in range(n_questions):
    qt, answer = map(str, input().split())
    qt = int(qt)
    remaining_time -= qt
    if remaining_time <= 0 and loser == -1:
        loser = current_player
    if answer == 'T':
        current_player = (current_player + 1) % 8
print(loser+1)
