# my_dict = {'总经理':99,'辣椒酱':88,'中西医':77}
# my_dict['中心站'] = 66
# print(f'字典新增元素后，结果：{my_dict}')
# my_dict['总经理'] = 33
# print(f'字典更新元素后，结果：{my_dict}')

# my_dict = {'总经理':99,'辣椒酱':88,'中西医':77}
# score = my_dict.pop('总经理')
# print(f'字典移除元素后，结果：{my_dict}，总经理的考试分数是：{score}')
# my_dict.clear()
# print(f'字典被清空了，内容是：{my_dict}')

# my_dict = {'总经理':99,'辣椒酱':88,'中西医':77}
# keys = my_dict.keys()
# print(f'字典的全部keys是：{keys}')
# # 遍历方式1
# for key in keys:
#     print(f'字典的keys是：{key}')
#     print(f'字典的value是：{my_dict[key]}')
# # 遍历方式2
# for key in my_dict:
#     print(f'2字典的keys是：{key}')
#     print(f'2字典的value是：{my_dict[key]}')

# my_dict = {'总经理':99,'辣椒酱':88,'中西医':77}
# num = len(my_dict)
# print(f'字典中的元素数量有{num}个')

my_dict = {
    '网络化':{
        '部门':'科技部',
        '工资':3000,
        '级别':1
    },'总经理':{
        '部门':'市场部',
        '工资':5000,
        '级别':2
    },'辣椒酱':{
        '部门':'市场部',
        '工资':7000,
        '级别':3
    },'中西医':{
        '部门':'科技部',
        '工资':4000,
        '级别':1
    },'领导好':{
        '部门':'市场部',
        '工资':6000,
        '级别':2}
}
for element in my_dict:
    if my_dict[element]['级别'] == 1:
        my_dict[element]['级别'] = 2
        my_dict[element]['工资'] += 1000
for element in my_dict:
    print(element,':',my_dict[element])

