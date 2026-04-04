# 定义一个字符串
text = "  Hello, world! Welcome to Python programming.   "

# 转换大小写
print("Upper:", text.upper())
print("Lower:", text.lower())
print("Capitalize:", text.capitalize())
print("Title:", text.title())

# 去除空白字符
print("Strip:", text.strip())
print("Lstrip:", text.lstrip())
print("Rstrip:", text.rstrip())

# 替换子串
replaced_text = text.replace("world","universe")
print("Replace:", replaced_text)

# 分割字符串
split_list = text.split()
print("Split:", split_list)

# 拼接字符串
joined_string = " ".join(split_list)
print("Join:", joined_string)

# 查找子串位置
find_index = text.find("world")
print("Find index of 'world':", find_index)

# 计算子串出现次数
count_occurrences = text.count("o")
print("Count occurrences of 'o':", count_occurrences)

