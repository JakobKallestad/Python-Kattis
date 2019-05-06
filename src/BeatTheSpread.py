n_test_cases = int(input())
for _ in range(n_test_cases):
    sum_scores, diff_scores = map(int, input().split())
    if sum_scores < diff_scores or sum_scores % 2 != diff_scores % 2:
        print("impossible")
        continue
    adder = (sum_scores-diff_scores)//2
    print(diff_scores+adder, adder)