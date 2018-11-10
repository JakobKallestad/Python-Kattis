import sys


def calc(a,b,c,i,j):
    if i == 0:
        if j == 0:
            if a == b+c:
                print(a,'=',b,'+',c,sep='')
                sys.exit()
        if j == 1:
            if a == b-c:
                print(a,'=',b,'-',c,sep='')
                sys.exit()
        if j == 2:
            if a == b*c:
                print(a,'=',b,'*',c,sep='')
                sys.exit()
        if j == 3:
            if a == b/c:
                print(a,'=',b,'/',c,sep='')
                sys.exit()
    else:
        if j == 0:
            if a + b == c:
                print(a,'+',b,'=',c,sep='')
                sys.exit()
        if j == 1:
            if a - b == c:
                print(a,'-',b,'=',c,sep='')
                sys.exit()
        if j == 2:
            if a * b == c:
                print(a,'*',b,'=',c,sep='')
                sys.exit()
        if j == 3:
            if a / b == c:
                print(a,'/',b,'=',c,sep='')
                sys.exit()


#(addition, subtraction, multiplication and division).
a, b, c = map(int, input().split())
for i in range(2):
    for j in range(4):
        calc(a,b,c,i,j)