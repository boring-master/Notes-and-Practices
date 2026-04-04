a = int(input('请输入一个数字：'))
b = int(input('请再输入一个数字：'))
# def add(x,y):
#     result = x + y
#     print(f'{x}+{y}的结果是：{result}')
# add(a,b)
def add(x,y):
    result = x + y
    return result
r = add(a,b)
print(f'{a}+{b}的结果是：',r)

