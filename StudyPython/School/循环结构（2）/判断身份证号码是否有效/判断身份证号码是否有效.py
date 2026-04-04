#判断身份证号是否有效
id=input("请输入身份证号：")
#代码开始
coe = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
sum = 0
num = [1,0,'X',9,8,7,6,5,4,3,2]
while True:
    if len(id) != 18:
        print('长度错误')
        break
    else:
        try:
            int(id[:17])
        except ValueError as e:
            print('存在无效字符')
            break
    for i in range(17):
        sum += int(id[i]) * coe[i]
    remainder = sum % 11
    if str(id[17]) == str(num[remainder]):
        print('正确校验码')
        break
    else:
        print('错误校验码')
        break
#代码结束
