# name = 'Andy'
# login_time = 10
# cost = 258.8890
# print('你好'+name+'，欢迎登录!这是您登录的第',login_time,'次',sep='')
# print('你好%s，欢迎登录!这是您登录的第%d次。您本次消费%.2f元'%(name,login_time,cost))

data = {'name':'Andy','login_time':10,'cost':258.88}
tuple_value = (data['name'],data['login_time'],data['cost'])
print('你好%s，欢迎登录!这是您登录的第%d次。您本次消费%.2f元' % tuple_value)

