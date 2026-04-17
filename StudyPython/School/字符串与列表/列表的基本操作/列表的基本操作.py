# 按注释要求完成列表操作函数定义
def list_operations(lst):
    '''
    #参数 lst:列表(数值型列表与非数值型列表两类)
    # return  无返回值,结果直接输出
    '''
    #####begin#####
    # 1 访问列表，检测列表中的元素是否都是数值类型：
    flag = 1  # 假设列表中全为数值型数据
    for x in lst:
        if not (type(x) == int or type(x) == float):
            flag = 0
            break
    # 1 如检测列表中的数据类型全不是数值类型，则完成下列操作：
    if flag == 0:
    # 1.1 删除列表的首尾元素并输出新列表
        first = lst.pop(0)
        last = lst.pop(-1)
        print(f'删除首尾元素后的列表:{lst}')
    # 1.2 将删除前的首元素添加到新列表的尾部，尾部元素添加到新列表的首部并输出
        lst.insert(0,last)
        lst.insert(len(lst)+2,first)
        print(f'插入首尾元素后的列表:{lst}')
    # 1.3 列表逆序并输出
        lst.reverse()
        print(f'逆序列表:{lst}')
    # 1.4 用列表推导式统计列表中每个元素的长度生成一个新的列表并输出。
        lst2 = [len(x) for x in lst]
        print(f'列表元素长度列表：{lst2}')
    # 1.5 输出最长列表元素，若有多个都一并输出
        mlen = max(len(x) for x in lst)
        lst3 = [x for x in lst if len(x) == mlen]
        for x in lst3:
            print(f'最长列表元素:{x}')
    # 2 所有元素都是数值数据(即 int 或 float 类型),若是则完成下列操作
    else:
    # 2.1 输出列表的最大值、最小值和总和
        ma = max(lst)
        mi = min(lst)
        print(f'列表的最大值:{ma},最小值:{mi},总和:{sum(lst)}')
    # 2.2 计算去掉一个最大值和一个最小值之后的列表均值，并输出该均值(保留4位小数)
        print(f'列表均值：{(sum(lst)-ma-mi)/(len(lst)-2):.4f}')
    # 2.3 对列表进行升序排列并输出排序后的结果
        lst.sort()
        print(f'升序排列列表:{lst}')
    # 2.4 输出列表三个最小值,按升序排列
        print(f'列表三个最小值,升序:{lst[:3]}')
    # 2.5 输出列表三个最大值,按降序排列
        lst2 = lst[-3:]
        lst2.reverse()
        print(f'列表三个最大值,降序:{lst2}')
    # 2.6 将列表中大于60的数据生成一个新的列表并输出
        lst3 = []
        for i in lst:
            if i > 60:
                lst3.append(i)
        print(f'大于60的新列表：{lst3}')
#######ends######

# 主程序代码不要修改
# 从键盘输入一个列表，完成函数调用
lst = eval(input())
list_operations(lst)
