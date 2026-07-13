def quickSort(alist):
    quickSortHelper(alist, 0, len(alist) - 1)
def quickSortHelper(alist, first, last):
    if first < last:
        # 交换部分元素的位置并把first位的元素交换到合适的位置，使其左边的元素都<它<右边的元素
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint - 1)
        quickSortHelper(alist, splitpoint + 1, last)
def partition(alist, first, last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1
        if rightmark < leftmark:
            done = True
        else:
            alist[rightmark], alist[leftmark] = alist[leftmark], alist[rightmark]
    alist[rightmark], alist[first] = alist[first], alist[rightmark]
    return rightmark

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist)
print(alist)