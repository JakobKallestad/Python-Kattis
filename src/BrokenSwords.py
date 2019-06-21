'''
4
0100
0010
0110
1010
'''

n_swords = int(input())
swords = [0, 0, 0, 0]
for _ in range(n_swords):
    sword = input()
    for i in range(4):
        if sword[i] == '0':
            swords[i] += 1
#print(swords)
a = min((swords[0]+swords[1])//2, (swords[2]+swords[3])//2)
b = swords[0]+swords[1]-2*a
c = swords[2]+swords[3]-2*a
print(a, b, c)