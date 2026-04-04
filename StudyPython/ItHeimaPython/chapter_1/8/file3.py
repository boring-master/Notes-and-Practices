# 打开不存在的文件
f = open('D:/test.txt','a',encoding='UTF-8')
f.write('黑马程序员')
f.flush()
f.close()

# 打开存在的文件
f = open('D:/test.txt','a',encoding='UTF-8')
f.write('学python最佳选择')
f.close()

