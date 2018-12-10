from collections import defaultdict

n_day = 1
while True:
    try:
        line = input()
        print("Day {}".format(n_day))
        n_day += 1
        park = {}
        customer_minutes = defaultdict(int)
        while True:
            customer = list(input().split())
            c_action = customer[0]
            if c_action == "CLOSE":
                break
            c_name = customer[1]
            c_time = int(customer[2])
            if c_action == "ENTER":
                park[c_name] = c_time
            else:
                customer_minutes[c_name] += (c_time-park[c_name])
        customer_minutes = sorted(customer_minutes.items(), key=lambda x: x[0])
        for cu in customer_minutes:
            print(cu[0], '${0:.2f}'.format(cu[1]*0.1))
        print()
    except:
        break
