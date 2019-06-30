
while True:
    try:
        line = input()
        result = eval(line)
        print("{:.2f}".format(result))
    except EOFError:
        break
