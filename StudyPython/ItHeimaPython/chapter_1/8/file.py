#f = open('E:/test.txt','r',encoding = 'UTF-8')
# print(type(f))

# print(f.read(10))
# print(f.read())

# lines = f.readlines()
# print(type(lines))
# print(lines)

# l1 = f.readline()
# l2 = f.readline()
# print(l1)
# print(l2)

# for line in f:
#     print(line)

# f.close()

with open('E:/test.txt','r',encoding = 'UTF-8') as f:
    for line in f:
        print(line)