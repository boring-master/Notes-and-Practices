my_list = [0,1,2,3,4,5,6]
result1 = my_list[1:4]   # 步长默认为1，可省略不写
print(f'结果1：{result1}')

my_tuple = (0,1,2,3,4,5,6)
result2 = my_tuple[:]     # 起始和结束不写表示从头到尾
print(f'结果2：{result2}')

my_str = '01234567'
result3 = my_str[::2]
print(f'结果3：{result3}')

my_str = '01234567'
result4 = my_str[::-1]
print(f'结果4：{result4}')

my_list = [0,1,2,3,4,5,6]
result5 = my_list[3:1:-1]
print(f'结果5：{result5}')

my_tuple = (0,1,2,3,4,5,6)
result6 = my_tuple[::-2]
print(f'结果6：{result6}')

