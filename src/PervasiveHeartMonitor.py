def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False

while True:
    try:
        line_list = input().split()
        full_name = [i for i in line_list if not isfloat(i)]
        beat_list = [float(i) for i in line_list if isfloat(i)]
        average_beat = sum(beat_list)/len(beat_list)
        print(average_beat, ' '.join(full_name))

    except EOFError:
        break
