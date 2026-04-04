#求给定范围内的所有素数
m=eval(input())  #输入范围
#代码开始
count = 0
flag = False
for i in range(2,m+1):
    if i == 2:
        print(i,end=' ')
        count += 1
    for j in range(2, i):
        if i % j == 0:
            flag = False
            break
        flag = True
    if flag:
        print(i,end=' ')
        count+=1
        if count % 10 == 0:
            print()
#代码结束
