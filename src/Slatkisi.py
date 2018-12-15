pay, n_zeros = map(int, input().split())

bills = 10 ** n_zeros
pay /= bills
pay = round(pay)
pay *= bills
print(pay)
