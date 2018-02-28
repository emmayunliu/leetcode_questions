def quickSort(list, first, last):
    if first < last:
        splitPoint = partition(list, first, last)
        quickSort(list, first, splitPoint-1)
        quickSort(list, splitPoint+1, last)

def partition(list, first, last):
    leftMark = first+1
    rightMark = last
    exchange = False
    while not exchange:
        while leftMark <= rightMark and list[leftMark] <= list[first]:
            leftMark += 1
        while leftMark <= rightMark and list[rightMark] >= list[first]:
            rightMark -= 1
        if leftMark > rightMark:
            exchange = True
        else:
            list[leftMark], list[rightMark] = list[rightMark], list[leftMark]
    list[first], list[rightMark] = list[rightMark], list[first]
    return rightMark


a_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(a_list, 0, len(a_list)-1)
print(a_list)
