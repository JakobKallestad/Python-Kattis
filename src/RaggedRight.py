line_list = []
max_length = 0
while True:
    try:
        line = input()
        if len(line) > max_length:
            max_length = len(line)
        line_list.append(line)
    except:
        break

del line_list[-1]
ragged_sum = 0
for line in line_list:
    ragged_sum += (max_length - len(line)) ** 2
print(ragged_sum)
