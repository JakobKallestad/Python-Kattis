n = int(input())
for i in range(n):
    sentence = input().split(" ")
    animal_sounds = set()
    while True:
        line = input()
        if line == "what does the fox say?":
            break;
        else:
           animal_sounds.add(line.split(" ")[2])

    result_list = []
    for sound in sentence:
        if sound not in animal_sounds:
            result_list.append(sound)
    print(" ".join(result_list))
