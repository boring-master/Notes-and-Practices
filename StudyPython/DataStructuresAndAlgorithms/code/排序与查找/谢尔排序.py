def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)
        print("After increments of size", sublistcount,"The list is", alist)
        sublistcount = sublistcount // 2
def gapInsertionSort(alist, start, gap):
    # 从start+gap开始以gap为间隔选取几个元素，对这几个元素进行排序
    for i in range(start + gap, len(alist), gap):
        position = i
        currentvalue = alist[position]
        while position >= gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position -= gap
        alist[position] = currentvalue

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shellSort(alist)
print(alist)