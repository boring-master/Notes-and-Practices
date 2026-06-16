x0 = eval(input('请输入根的初始值:'))  # 该输入作为第0个初始根
x1 = eval(input('请输入根的初始值:'))  # 该输入作为第1个初始根

err = 1e-6  # 误差，要求根处的函数值的绝对值小于误差err
###############begin##################
def f(x):
    return x**3 - x - 1

max_iter = 1000  
count = 0
f0 = f(x0)
f1 = f(x1)

if f0 == f1:
    print("root=False")
    print('迭代次数=0')
else:
    found = False
    while count < max_iter:
        count += 1

        denominator = f1 - f0
        if denominator == 0:
            break
        x2 = x1 - f1 * (x1 - x0) / denominator
        f2 = f(x2)
        if abs(f2) < err:
            print(f"root={x2:.6f}")
            print(f'迭代次数={count}')
            found = True
            break
        x0, f0 = x1, f1
        x1, f1 = x2, f2

    if not found:
        print("root=False")
        print(f'迭代次数={count}')
###############end###################