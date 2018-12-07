binary_dict = {'000': '0', '001': '1', '010': '2', '011': '3', '100': '4', '101': '5', '110': '6', '111': '7'}
line = list(input())
while len(line) % 3 != 0:
    line.insert(0, '0')
fin = []
for i in range(0, len(line), 3):
    fin.append(binary_dict[''.join(line[i:i+3])])
print(''.join(fin))