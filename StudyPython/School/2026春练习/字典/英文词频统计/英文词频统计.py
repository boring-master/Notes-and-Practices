# 输入的字符串中可包含".,~!@#$%^&*()+_/0123456789"等非英文单词字符
WordStr = input()
# 1:归一化处理
WordStr = WordStr.lower()
for word in WordStr:
    if word in '.,~!:@#$%^&*()+_/0123456789':
        WordStr = WordStr.replace(word, ' ')
# 2分割字符串为列表,英文单词之间用空格分隔
WordLst = WordStr.split()
# 3 统计每个单词的个数（列表或字典的方法）
WordDict = {}
for word in WordLst:
    WordDict[word] = WordDict.get(word, 0) + 1
    # if word not in WordDict:
    #     WordDict[word] = 1
    # else:
    #     WordDict[word] += 1
# 字典排序,返回值是一个列表 ?
# 输出最高频率单词和次数 ,多个相同高频字也要输出
max = 0
for value in WordDict.values():
    if value > max:
        max = value
for key, value in WordDict.items():
    if value == max:
        print(key,value)