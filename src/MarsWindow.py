year = int(input())-2018
print("yes" if any([m%26==0 for m in range(year*12-3, year*12+9)]) else "no")
