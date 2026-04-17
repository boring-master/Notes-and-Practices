# 按注释要求完成序列操作函数定义
def sequence_operations(seq):
    '''
    #参数 seq:序列数据可以是字符串或列表或元组
    # return  无返回值,结果直接输出
    '''
    #####begin#####
    # 1计算并输出序列的长度
    print(f'序列长度:{len(seq)}')
    # 输出序列的第一个和最后一个元素的值
    print(f'序列首元素:{seq[0]},尾元素:{seq[-1]}')
    # 逆序输出序列
    print(f'逆序序列:{seq[::-1]}')
    # 用"+"或"*"运算复制序列并输出
    print(f'序列复制:{seq*2}')
    # 判断序列类型,若为字符串，则检测字符串是否全为数字字符，若是将其转换成整数求和并输出，否则输出"非数字字符"
    # 若为列表，检测序列中的所有元素是否都是数值数据(即 int 或 float 类型),若是则计算并输出这些数据的均值，结果保留1位小数；否则，输出 "非数字列表"。
    # 若为元组，则输出排序前元组与排序后的序列数据
    if isinstance(seq, str):
        if seq.isdigit():
            total = sum(int(digit) for digit in seq)
            print(f'字符数字和:{total}')
        else:
            print(f"{seq}是非数字字符")

    if isinstance(seq, list):
        if all(isinstance(item, (int, float)) for item in seq):
            average = sum(seq) / len(seq)
            print(f"列表均值:{average:.1f}")
        else:
            print(f"{seq}是非数字列表")

    if isinstance(seq, tuple):
        sorted_tuple = list(sorted(seq))
        print(f"原序列：{seq}")
        print(f"排序后的序列:{sorted_tuple}")
    #######ends######


# 主程序代码不要修改
# 从键盘输入一个序列，完成函数调用
seq = input()
if (seq[0] == "[" and seq[-1] == "]") or (seq[0] == "(" and seq[-1] == ")"):
    seq = eval(seq)
sequence_operations(seq)