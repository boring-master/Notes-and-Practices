#n个钱买n只鸡问题
print("依次输出公鸡 母鸡 小鸡的数量：")
n=eval(input()) #n表示钱的总数和鸡的总数
#代码开始
for i in range(int(n/5)):
    for j in range(int((n-i)/3)):
        if (n-i-j)%3==0 and (n-5*i-3*j)*3 == n-i-j:
            print(f'{i} {j} {n-i-j}')
#代码结束