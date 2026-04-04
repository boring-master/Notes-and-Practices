def tes_func(compute):
    result = compute(1,2)
    print(type(compute))
    print(f'计算结果：{result}')

def compute(x,y):
    return x + y
tes_func(compute)

