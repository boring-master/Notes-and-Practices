# 完成绘制钻石图案函数定义
def draw_str(n):
    """
    #参数n : int,表示输出图案的行数
    #returns ：None.
    """
    #######begin######
    for i in range(1,n+1):
        print(' '*(n-i),end='')
        print('*'*(2*i-1))
    for j in range(1,n):
        print(' '*j,end='')
        print('*'*((n-j)*2-1))
    #######ends#######
# 主程序不要修改
col = eval(input())  # 图案行数输入
draw_str(col)  # 调用函数完成图案的输出



