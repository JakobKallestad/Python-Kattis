while True:
    try:
        print("yes") if "problem" in input().casefold() else print("no")
    except:
        break