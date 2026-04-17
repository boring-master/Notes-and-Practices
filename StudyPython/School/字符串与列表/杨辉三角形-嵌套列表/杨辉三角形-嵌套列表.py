# 计算并绘制杨辉三角形
def draw_yh(n):
    """
     参数n : int 杨辉三角的行数
     返回值：无,直接输出
    """
    #########begin##############
    lst = []
    for i in range(0,n):
        temp = []
        for j in range(0,i+1):
            if j == 0 or j == i:
                temp.append(1)
            else:
                a = lst[i-1][j-1] + lst[i-1][j]
                temp.append(a)
        lst.append(temp)
    for i in lst:
        print(i)
    #########ends##############


# 主程序
num = int(input())  # num为杨辉三角的行数
draw_yh(num)

