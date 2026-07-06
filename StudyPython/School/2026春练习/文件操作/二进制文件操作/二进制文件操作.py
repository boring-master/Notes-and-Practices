#输入字节数n
n=eval(input())
#打开图片文件example.png，读取前n字节,保存到example_new.png中
############begin############
with open('example.png','rb') as f, open('example_new.png','wb') as g:
    g.write(f.read(n))
#############end#############
#输出新文件内容
with open('example_new.png','rb') as f2:
    print(f2.read())