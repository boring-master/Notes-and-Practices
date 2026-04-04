# my_set = {'传智教育','黑马程序员','itheima','传智教育',
#           '黑马程序员','itheima','传智教育','黑马程序员','itheima'}
# my_set_empty = set()   # 定义空集合
# print(f'my_set的内容是：{my_set}，类型是：{type(my_set)}')
# print(f'my_set_empty的内容是：{my_set_empty}，类型是：{type(my_set_empty)}')

# my_set = {'传智教育','黑马程序员','itheima'}
# my_set.add('Python')
# my_set.add('传智教育')
# print(f'my_set添加元素后结果是：{my_set}')

# my_set = {'传智教育','黑马程序员','itheima'}
# my_set.remove('黑马程序员')
# print(f'my_set移除黑马程序员后，结果是：{my_set}')

# my_set = {'传智教育','黑马程序员','itheima'}
# element = my_set.pop()
# print(f'集合被取出的元素是：{element}，取出元素后：{my_set}')

# my_set = {'传智教育','黑马程序员','itheima'}
# my_set.clear()
# print(f'集合被清空了，结果是：{my_set}')

# set1 = {1,2,3}
# set2 = {1,5,6}
# set3 = set1.difference(set2)
# print(set3)
# print(set2)
# print(set1)

# set1 = {1,2,3}
# set2 = {1,5,6}
# set1.difference_update(set2)
# print(set1)
# print(set2)

# set1 = {1,2,3}
# set2 = {1,5,6}
# set3 = set1.union(set2)
# print(set3)
# print(set2)
# print(set1)

# set1 ={1,2,3,4,5,6,7}
# num = len(set1)
# print(f'集合内的元素数量有：{num}')

# set1 ={1,2,3,4,5,6,7}
# for element in set1:
#     print(f'集合的元素有：{element}')

my_list = ['黑马程序员','传智播客','黑马程序员','传智播客','itheima','itcast','itheima','itcast','best']
set_empty = set()
for element in my_list:
    set_empty.add(element)
print(set_empty)