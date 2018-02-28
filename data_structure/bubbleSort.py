def bubbleSort(list):
    for i in range(0, len(list)-1):
        done = False
        position = i
        while not done and position < len(list)-1:
            if list[position] <= list[position+1]:
                done = True
            else:
                list[position], list[position+1] = list[position+1], list[position]
                position += 1
    return list


a_list=[20, 40, 30, 90, 50, 80, 70, 60, 110, 100]
bubbleSort(a_list)
print(a_list)