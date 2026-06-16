import math

x = eval(input('请输入x的初值:'))
lr = eval(input('请输入学习率:'))  # 学习率，
precision = 1e-6  # 设置收敛精度,f'(x)与0值的差异
max_iters = 10000  # 最大迭代次数
###################begin############
found = False
iter_count = 0

for i in range(max_iters):
    if x == 0:
        break

    grad = -0.1 * math.cos(x / 10.0) - (1.0 / 3.0) * (x ** (-2.0 / 3.0))

    if abs(grad) < precision:
        found = True
        iter_count = i
        break

    x = x - lr * grad

if found:
    y = -math.sin(x / 10.0) - (x ** (1.0 / 3.0))
    print(f"x={x:.6f}")
    print(f"最小值={y:.6f}")
    print(f'迭代次数={iter_count}')
else:
    print("False")
##################end#######################

