# 1定义一个判断一个数是否是素数的函数，如果是输出1，否则输出0
#######begin########
def isprime(x):
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return 0
    return 1
#######ends########

# 2调用isprime()函数求两位数内的绝对素数并输出
#######begin########
for x in range(10,100):
    if isprime(x) and isprime(x%10*10+x//10):
            print(f'{x}和{x%10*10+x//10}是绝对素数')
#######ends########
print('*' * 20)

# 3定义一验证歌德巴赫猜想函数
def Goldbach(N):  # 将N分解成两素数之和
    if N < 6 or N % 2 == 1:  # 若N小于6或N为奇数
        print('N应该是大于等于6的偶数')
    else:
        # 循环判断，得到符合要求的小于N的两个素数，并打印
        for x in range(2, N // 2 + 1):  # 想想为什么是从2到N/2
            # 调用isPrime函数得到符合要求的小于N的两个素数
            ######## begin ###########
            if isprime(x) and isprime(N-x):
            ######## end ###########
                print(N, '=', x, '+', N - x)
                break

for num in [88, 68, 50, 1000]:
    Goldbach(num)
print('*' * 20)

