a, b, c = map(int, input().split())
play_time = -1
if abs(a-b) < abs(b-c):
    while a < c and b < c:
        play_time += 1
        if a <b:
            a = b+1
        else:
            b = a+1
else:
    while c > a and b > a:
        play_time += 1
        if c > b:
            c = b-1
        else:
            b = c-1

print(play_time)