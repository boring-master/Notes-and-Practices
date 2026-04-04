#打印字母图形
n = eval(input())  #输入行数
#代码开始
for i in range(1,n+1):
    print(' '*(n-i),end='')
    for j in range(i,0,-1):
        m = ord('A') - 1
        print(chr(m+j),end='')
    for k in range(1,i,1):
        m = ord('A')
        print(chr(m+k),end='')
    print()   #换行
#代码结束