bottle_a, bottle_b, price = map(int, input().split())
remaining_bottles = bottle_a + bottle_b
drank = 0

while remaining_bottles >= price:
    #print(remaining_bottles, drank)
    new_empties = int(remaining_bottles/price)
    drank += new_empties
    remaining_bottles %= price
    remaining_bottles += new_empties
print(drank)