
#求s= a + aa + aaa + … + aa…a
a=eval(input())   #输入a值
n=eval(input())   #输入最后一项中 a 的个数 n
#代码开始
s = 0
t = 0
for i in range(n):
    t += a*(10**i)
    s += t
print(s)
#代码结束
