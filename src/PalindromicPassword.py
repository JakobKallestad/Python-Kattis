from bisect import bisect

palindromes = []
for i in range(100000, 1000000):
    if str(i) == str(i)[::-1]:
        palindromes.append(i)
n_test_cases = int(input())
for _ in range(n_test_cases):
    n = int(input())
    low_ind = bisect(palindromes, n)-1
    if abs(palindromes[low_ind]-n) <= abs(palindromes[low_ind+1]-n):
        print(palindromes[low_ind])
    else:
        print(palindromes[low_ind+1])
