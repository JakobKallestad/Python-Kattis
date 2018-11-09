n = int(input())
for i in range(n):
    input_list = list(map(int, input().split(" ")))
    n_points = input_list[0]

    x_list = []
    y_list = []

    for i in range(1,n_points*2,2):
        x_list.append(input_list[i])
        y_list.append(input_list[i+1])
    #print(x_list)
    #print(y_list)

    area_1 = 0
    area_2 = 0
    for i in range(n_points):
        m_index = (i+1)%n_points
        area_1 += x_list[i]*y_list[m_index]
        area_2 += y_list[i]*x_list[m_index]

    area = (area_1-area_2)/2
    print(area)
