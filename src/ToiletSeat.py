seq = list(input())

adjustments = seq[1:].count('D')*2
if seq[0] == seq[1] == 'D':
    adjustments -= 1
elif seq[0] == 'D':
    adjustments += 1
print(adjustments)

current_seat = seq[0]
adjustments = seq[1:].count('U')*2
if seq[0] == seq[1] == 'U':
    adjustments -= 1
elif seq[0] == 'U':
    adjustments += 1
print(adjustments)

current_seat = seq[0]
adjustments = 0
for person in seq[1:]:
    if person != current_seat:
        adjustments +=1
        current_seat = person
print(adjustments)