# def list_while_func():
#     mylist = ['传智教育','黑马程序员','Python']
#     index = 0
#     while index < len(mylist):
#         element = mylist[index]
#         print(f'列表的元素：{element}')
#         index += 1
# list_while_func()
#
# def list_for_func():
#     mylist = [1,2,3,4,5]
#     for element in mylist:
#         print(f'列表的元素有：{element}')
# list_for_func()

def while_f():
    list0 = [1,2,3,4,5,6,7,8,9,10]
    index = 0
    list1 = []
    while index < len(list0):
        element = list0[index]
        if element % 2 == 0:
            list1.append(element)
        index += 1
    print(list1)
while_f()

def for_f():
    list0 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list1 = []
    for element in list0:
        if element % 2 == 0:
            list1.append(element)
    print(list1)
for_f()

