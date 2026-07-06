import numpy as np

seed1, seed2 = eval(input('请输入随机数种子:'))
lr = eval(input('请输入学习率:'))  # lr是学习率
np.random.seed(seed1)
x = np.random.randn()  # 二元函数f(x,y)中，自变量x的初值
np.random.seed(seed2)
y = np.random.randn()  # 二元函数f(x,y)中，自变量y的初值
err = 1e-6  ##误差，要求最小值处的函数的两个偏导数的绝对值都小于误差err
max_iters = 10000  # 最大迭代次数

# 请用梯度下降法求出给定二元函数f(x,y)的最值及相关信息
##################begin################
def f(x, y):
    return x**3 - y**3 + 3*x**2 + 3*y**2 - 9*x

def dx(x, y):
    return 3*(x**2) + 6*x - 9

def dy(x, y):
    return -3*(y**2) + 6*y

for t in range(max_iters):
    grad_x = dx(x, y)
    grad_y = dy(x, y)
    if abs(grad_x) < err and abs(grad_y) < err:
        print("迭代次数%d,x=%.8f,y=%.8f,f(x,y)=%.8f" % (t , x, y, f(x, y)))
        break
    x = x - lr * grad_x  # 请更新x值
    y = y - lr * grad_y  # 请更新y值
else:
    print('False')
###################end#######################