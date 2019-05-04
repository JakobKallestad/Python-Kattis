word_to_value = {}

while True:
    try:
        line = input().split()
        if len(line) == 3:
            word_to_value[line[2]] = int(line[1])
        else:
            if line[1] not in word_to_value or line[3] not in word_to_value:
                print("undefined")
            else:
                if line[2] == '<':
                    if word_to_value[line[1]] < word_to_value[line[3]]:
                        print("true")
                    else:
                        print("false")
                elif line[2] == '>':
                    if word_to_value[line[1]] > word_to_value[line[3]]:
                        print("true")
                    else:
                        print("false")
                else:
                    if word_to_value[line[1]] == word_to_value[line[3]]:
                        print("true")
                    else:
                        print("false")
    except EOFError:
        break
