a = eval(input('输入根的左边界:'))
b = eval(input('输入根的右边界:'))
err = 1e-6  # 误差，要求根处的函数值的绝对值小于误差err
########请用二分法求方程的根begin#######
def f(x):
    return x**3 - x - 1

count = 0
fa = f(a)
fb = f(b)

if fa * fb >= 0:
    print("root=False")
    print('迭代次数:0')
else:
    while True:
        count += 1
        x = (a + b) / 2.0
        fx = f(x)
        if abs(fx) < err:
            print(f"root={x:.6f}")
            print(f'迭代次数:{count}')
            break
        if fx * fa > 0:
            a = x
            fa = fx
        else:
            b = x
            fb = fx
#########end##########################