n_papers = int(input())
papers = []
for _ in range(n_papers):
    papers.append(int(input()))
papers.sort()

for i, p in enumerate(papers):
    if n_papers-i <= p:
        print(n_papers-i)
        break

else:
    print(0)
