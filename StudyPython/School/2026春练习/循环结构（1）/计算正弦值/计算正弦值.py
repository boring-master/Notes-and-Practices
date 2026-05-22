#求正弦值
from math import *

x = eval(input())  #输入弧度值
#代码开始
term = x
result = 0
n = 1
while abs(term) >= 1e-7:
    result += term
    n += 2
    term *= -x * x / (n * (n - 1))
print(f'{result:.7f}')
#代码结束
