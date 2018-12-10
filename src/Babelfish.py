dct = {}
dct_keys = set()
while True:
    line = input()
    if line == "":
        break
    value, key = map(str, line.split())
    dct[key] = value
    dct_keys.add(key)

while True:
    try:
        line = input()
        if line in dct_keys:
            print(dct[line])
        else:
            print("eh")
    except:
        break
