from fractions import Fraction
up, down = map(int, input().split('/'))
fr = Fraction(up, down)
fr -= 32
fr *= 5
fr /= 9
print(fr, end='')
if fr.denominator == 1:
    print("/1")
