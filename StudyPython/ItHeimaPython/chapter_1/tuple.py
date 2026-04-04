# t1 = (1,'Hello',True)
# t2 = ()             # 空元组
# t3 = tuple()        # 空元组
# print(f't1的类型是：{type(t1)}，内容是：{t1}')
# print(f't2的类型是：{type(t2)}，内容是：{t2}')
# print(f't3的类型是：{type(t3)}，内容是：{t3}')

# t4 = ('hello')
# print(f't4的类型是：{type(t4)}，t4的内容是：{t4}')
# t5 = ('hello',)
# print(f't5的类型是：{type(t5)}，t5的内容是：{t5}')

# t6 = ((1,2,3),(4,5,6))
# print(f't6的类型是：{type(t6)}，t6的内容是：{t6}')
# num = t6[1][2]
# print(f'从嵌套元组中取出的数据是：{num}')

# t7 = ('传智教育','黑马程序员','黑马程序员','黑马程序员','Python')
# index = 0
# while index < len(t7):
#     print(f'1元组的元素有‘{t7[index]}')
#     index += 1
#
# for element in t7:
#     print(f'2元组的元素有‘{element}')

# t8 = (1,2,['itheima','itcast'])
# print(f't8的内容是：{t8}')
# t8[2][0] = '黑马程序员'
# t8[2][1] = '传智教育'
# print(f't8的内容是：{t8}')

tu = ('周杰伦',11,['football','music'])
address1 = tu.index(11)
print(f'年龄所在位置为：{address1}')
print(f'学生的姓名为：{tu[0]}')
del tu[2][0]
tu[2].append('coding')
print(tu)
