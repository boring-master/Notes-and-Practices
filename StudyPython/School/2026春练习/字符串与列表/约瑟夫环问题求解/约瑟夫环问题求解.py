# 定义约瑟夫函数完成出圈列表
def jos_func(n, m):
    """
     参数n,m : int n代表总人数,m代表出圈间隔序号数
     返回值：list:出圈列表
    """
    result = []  # 出圈列表
    #########begin##############
    inilst = list(range(1,n+1))
    current_pos = 0
    while inilst:
        current_pos = (current_pos + m - 1) % len(inilst)
        removed = inilst.pop(current_pos)
        result.append(removed)
    #########ends##############
    return (result)
###############################
# 主程序
n, m = eval(input())
jos_lst = jos_func(n, m)
print("出圈列表:")
print(jos_lst)