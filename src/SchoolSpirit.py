uni_score = 0
student_scores = []

n = int(input())
for i in range(n):
    score = int(input())
    student_scores.append(score)
    uni_score += score*(4/5)**i

avg_g = 0
for i, _ in enumerate(student_scores):
    g = 0
    k = 0
    for j, s in enumerate(student_scores):
        if i == j:
            continue
        g += s*(4/5)**k
        k += 1
    avg_g += g/5
avg_g /= n

print(uni_score/5)
print(avg_g)

