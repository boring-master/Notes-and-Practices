x = eval(input('请输入根的初值：'))
h = eval(input('请输入搜索步长：'))
err = 1e-6  # 误差，要求根处的函数值的绝对值小于误差err
############begin#########
def f(x):
    return x**3 - x - 1

count = 0
found = False

fx = f(x)
if fx > 0 and abs(fx) >= err:
    print("root=False")
    print(f'迭代次数:0')
else:
    while x <= 10.0:
        count += 1
        fx = f(x)
        if abs(fx) < err:
            print(f"root={x:.4f}")
            print(f'迭代次数:{count-1}')
            found = True
            break
        if fx > 0:
            print("root=False")
            print(f'迭代次数:{count-1}')
            found = True
            break
        x += h
    if not found:
        print("root=False")
        print(f'迭代次数:{count-1}')
##############end##########