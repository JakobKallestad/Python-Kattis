friend_correct = int(input())
your = input()
friend = input()
max_correct = len(your)
n_equal_answer = 0
for c1, c2 in zip(your, friend):
    if c1 == c2:
        n_equal_answer += 1
max_correct -= abs(n_equal_answer-friend_correct)
print(max_correct)