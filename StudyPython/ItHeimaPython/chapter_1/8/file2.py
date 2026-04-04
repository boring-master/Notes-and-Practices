# 打开不存在的文件
f = open('D:/test.txt','w',encoding='UTF-8')
f.write('Hello World!')
f.flush()
f.close()

# 打开存在的文件
f = open('D:/test.txt','w',encoding='UTF-8')
f.write('黑马程序员')
f.close()

