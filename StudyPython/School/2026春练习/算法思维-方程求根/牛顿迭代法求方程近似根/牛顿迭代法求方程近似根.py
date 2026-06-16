x=eval(input('请输入根的初始值:'))
err=1e-6 #误差，要求根处的函数值的绝对值小于误差err
#################begin##############
def f(x):
    return x**3 - x - 1

def df(x):
    return 3 * x**2 - 1

count = 0

while abs(f(x)) >= err:
    fx = f(x)
    dfx = df(x)
    if dfx == 0:
        print("root=False")
        print(f'迭代次数={count}')
        break
    x = x - fx / dfx
    count += 1
else:
    print(f"root={x:.6f}")
    print(f'迭代次数={count}')
##################end###############