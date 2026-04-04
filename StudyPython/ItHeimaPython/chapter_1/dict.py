# my_dict1 = {'网络化':99,'总经理':88,'辣椒酱':77}
# my_dict2 = {}
# my_dict3 = dict()
# print(f'字典1的内容是：{my_dict1},类型：{type(my_dict1)}')
# print(f'字典2的内容是：{my_dict2},类型：{type(my_dict2)}')
# print(f'字典3的内容是：{my_dict3},类型：{type(my_dict3)}')

# my_dict1 = {'网络化':99,'总经理':88,'辣椒酱':77}
# print(my_dict1['网络化'])

stu_score_dict = {
    '网络化':{
        '语文':77,
        '数学':66,
        '英语':33
    },'总经理':{
        '语文':88,
        '数学':86,
        '英语':55
    },'辣椒酱':{
        '语文':99,
        '数学':96,
        '英语':66
    }
}
score = stu_score_dict['总经理']['语文']
print(score)


