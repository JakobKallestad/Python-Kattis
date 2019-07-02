n, k = map(int, input().split())
commands = list(input().split())
stack = [0]
ind = 0
while ind < len(commands):
    co = commands[ind]
    if co.lstrip('-').isdigit():
        to = (stack[-1]+int(co))%n
        if to < 0:
            to = n-to
        stack.append(to)
    else:
        ind += 1
        for _ in range(int(commands[ind])):
            stack.pop()
    ind += 1
print(stack[-1])
