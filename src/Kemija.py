str = input()
fin_str = []
vowel_list = ['a', 'e', 'i', 'o', 'u']
wait_time = 0
for c in str:
    if wait_time>0:
        wait_time-=1
        continue
    if c in vowel_list:
        wait_time+=2
    fin_str.append(c)
print("".join(fin_str))
