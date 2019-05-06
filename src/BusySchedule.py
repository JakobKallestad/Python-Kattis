while True:
    n_appointments = int(input())
    if n_appointments == 0:
        break
    appointments = []
    for _ in range(n_appointments):
        original_time = input()
        time = original_time.split(":")
        hour = int(time[0]) % 12
        time = time[1].split(" ")
        minute = time[0]
        ampm = time[1]
        if ampm == "p.m.":
            hour += 12
        appointments.append((int(str(hour) + str(minute)), original_time))
    appointments = sorted(appointments, key=lambda x: x[0])
    for _, time_str in appointments:
        print(time_str)
    print()
