str1 = 'itheima'
str2 = 'itcast'
str3 = 'python'
count = 0
for i in str1:
    count += 1
print(f'字符串{str1}的长度是：{count}')
count = 0
for i in str2:
    count += 1
print(f'字符串{str2}的长度是：{count}')
count = 0
for i in str3:
    count += 1
print(f'字符串{str3}的长度是：{count}')

def len(data):
    count = 0
    for i in data:
        count += 1
    print(f'字符串{data}的长度是{count}')
len(str1)
len(str2)
len(str3)

