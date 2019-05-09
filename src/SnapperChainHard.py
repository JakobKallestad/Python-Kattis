n_test_cases = int(input())
on_click = {i: 2 ** i for i in range(1, 31)}
for i in range(1, n_test_cases + 1):
    n, k = map(int, input().split())
    is_on = "OFF"
    if k % on_click[n] == on_click[n] - 1:
        is_on = "ON"
    print("Case #{}: {}".format(i, is_on))

