while True:
    try:
        month, date, year, start, end = input().split()
        start_h, start_m = map(int, start.split(':'))
        end_h, end_m = map(int, end.split(':'))
        result_m = (60 - start_m + end_m) % 60
        result_h = end_h - start_h
        if start_m > end_m:
            result_h -= 1
        print(month, date, year, result_h, "hours", result_m, "minutes")

    except:
        break
