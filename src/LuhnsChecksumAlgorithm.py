def lun_transform(n):
    n *= 2
    n_num = 0
    while n > 0:
        n_num += n % 10
        n //= 10
    return n_num


if __name__ == "__main__":
    cases = int(input())
    for _ in range(cases):
        chars = [int(c) for c in input()]
        chars = chars[::-1]
        chars[1::2] = [lun_transform(n) for n in chars[1::2]]
        char_sum = sum(chars)
        print("PASS") if char_sum % 10 == 0 else print("FAIL")