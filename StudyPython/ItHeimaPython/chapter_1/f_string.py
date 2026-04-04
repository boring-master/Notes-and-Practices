name = 'Andy'
login_time = 10
cost = 258.8890
# print('你好'+name+'，欢迎登录!这是您登录的第',login_time,'次',sep='')
# print('你好%s，欢迎登录!这是您登录的第%d次。您本次消费%.2f元'%(name,login_time,cost))
# print('你好{a}，欢迎登录!这是您登录的第{b}次。您本次消费{c:.2f}元。恭喜{a}成为vip'.format(a=name,b=login_time,c=cost))
print(f'你好{name}，欢迎登录!这是您登录的第{login_time}次。您本次消费{cost:.2f}元。恭喜{name}成为vip')


