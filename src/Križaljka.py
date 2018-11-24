def find_crosses(w1, w2):
    for i, a in enumerate(w1):
        for j, b in enumerate(w2):
            if a == b:
                return i, j


def display(w1, w2, cross_x, cross_y):
    row_list = ['.']*len(w1)
    for i in range(len(w2)):
        row_list = ['.']*len(w1)
        row_list[cross_x] = w2[i]
        if i == cross_y:
            row_list = [c for c in w1]
        print(''.join(row_list))




if __name__ == "__main__":
    w1, w2 = input().split()
    cross_x, cross_y = find_crosses(w1, w2)
    display(w1, w2, cross_x, cross_y)
