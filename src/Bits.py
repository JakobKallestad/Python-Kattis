n_test_cases = int(input())
for _ in range(n_test_cases):
    line = input()
    max_bits = 0
    for i in range(1, len(line)+1):
        num = bin(int(line[:i]))
        max_bits = max(max_bits, num.count('1'))
    print(max_bits)