# 定义2个lambda函数，求3个数的最大值max1,和最小值min1的函数
##########begin##########
ma = lambda x,y,z:max(x,y,z)
mi = lambda x,y,z:min(x,y,z)
##########ends##########

# 从键盘输入3个数，调用max1和min1函数完成求3个数的最大值和最小值的程序，输出最大值和最小值
##########begin##########
a,b,c = eval(input())
print(f'{ma(a,b,c)} {mi(a,b,c)}')
##########ends##########