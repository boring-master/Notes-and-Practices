#剩余材料最短
length=eval(input())   #输入钢管长度
n=0      #19米为n段
m=0      #23米为m段
rest=length   #剩余材料长度
#代码开始
n = int(length/19)
for i in range(1,int(length/23)+1):
    for j in range(1,int((length-23*i)/19)+1):
        n_rest = length-23*i-19*j
        if n_rest < rest:
            rest = n_rest
            n = j
            m = i
        if n_rest == rest:
            if j < n :
                n = j
                m = i
#代码结束
print("切割方案：19米{}段,23米{}段,剩余{}米.".format(n,m,rest))


