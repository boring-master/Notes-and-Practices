# # 捕获常规异常
# try:
#     f = open('D:/abc.txt','r',encoding='utf-8')
# except:
#     print('出现异常了，改打开模式')
#     f = open('D:/abc.txt','w',encoding='utf-8')
from tkinter.font import names

# # 捕获指定异常
# try:
#     # print(name)
#     1/0
# except NameError as e:
#     print('出现了变量未定义的异常')

# # 捕获多个异常
# try:
#     # 1/0
#     print(name)
# except(NameError,ZeroDivisionError) as e:
#     print('出现了变量未定义的异常 或者 除以0的异常错误')

# # 捕获所有异常
# try:
#     open('bill.txt')
#     1/0
#     print(name)
# except Exception as e:
#     print('出现异常了')

# try:
#     print('hello')
# except Exception as e:
#     print('出现异常了')
# else:
#     print('好高兴，没有异常')

try:
    f = open('D:/bill.txt', 'r', encoding='utf-8')
except Exception as e:
    print('出现异常了')
    f = open('D:/bill.txt', 'w', encoding='utf-8')
else:
    print('好高兴，没有异常')
finally:
    f.close()
